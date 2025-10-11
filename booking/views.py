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

    return render(request, 'booking/book_appointment.html', {'form': form})


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