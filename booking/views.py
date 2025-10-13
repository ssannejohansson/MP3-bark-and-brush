from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import JsonResponse
from .models import Appointment, TIME_CHOICES
from .forms import AppointmentForm
from django.utils.dateparse import parse_date
from . import models
from django.contrib import messages
import datetime
from django.shortcuts import get_object_or_404


# Create your views here.
@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.booked_on = now()

            # Prevent double-booking as backup
            if Appointment.objects.filter(day=appointment.day, time=appointment.time).exists():
                messages.error(request, "That time slot is already booked. Please choose another.")
            else:
                appointment.save()
                messages.success(request, "Appointment booked successfully!")
                return redirect('appointment_success')
    else:
        form = AppointmentForm()

    return render(request, 'booking/book_appointment.html', {'appointment_form': form})


def get_available_times(request):
    selected_date = request.GET.get('day')
    if not selected_date:
        return JsonResponse({'error': 'No date provided'}, status=400)

    selected_date = parse_date(selected_date)
    all_times = [t[0] for t in TIME_CHOICES]

    # Get already-booked times for that day
    booked_times = Appointment.objects.filter(day=selected_date).values_list('time', flat=True)

    # Filter out booked times
    available_times = [t for t in all_times if t not in booked_times]

    return JsonResponse({'available_times': available_times})


def get_fully_booked_dates(request):
    today = datetime.date.today()
    next_30_days = [today + datetime.timedelta(days=i) for i in range(30)]
    fully_booked = []

    for day in next_30_days:
        booked_times = Appointment.objects.filter(day=day).values_list('time', flat=True)
        if len(booked_times) >= len(TIME_CHOICES):
            fully_booked.append(day.isoformat())

    return JsonResponse({'fully_booked_dates': fully_booked})


@login_required
def appointment_success(request):
    latest_appointment = (
        Appointment.objects.filter(user=request.user)
        .order_by('-booked_on')
        .first()
    )
    return render(request, 'booking/appointment_success.html', {
        'appointment': latest_appointment
    })



@login_required
def update_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)

    if request.method == 'POST':
        if 'delete' in request.POST:
            appointment.delete()
            messages.success(request, "Appointment canceled.")
            return redirect('book_appointment')

        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment updated.")
            return redirect('appointment_success')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'booking/update_appointment.html', {
        'form': form,
        'appointment': appointment
    })

@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user).order_by('day', 'time')
    return render(request, 'booking/my_appointments.html', {
        'appointments': appointments
    })