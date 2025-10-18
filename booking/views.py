import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.utils.dateparse import parse_date
from .models import Appointment, TIME_CHOICES
from .forms import AppointmentForm


# Create your views here.
@login_required
def book_appointment(request):
    """
    Handle new appointment bookings
    Logged in users can submit the form to create an appointment
    """
    if request.method == "POST":
        # user=request.user to auto-fill logged in users information
        form = AppointmentForm(request.POST, user=request.user)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.booked_on = now()

            # Prevent double-booking
            if Appointment.objects.filter(
                day=appointment.day, time=appointment.time
            ).exists():
                messages.error(
                    request, "That time slot is already booked. Please choose another."     # noqa
                )
            else:
                appointment.save()
                messages.success(request, "Appointment booked successfully!")
                return redirect("appointment_success")
    else:
        form = AppointmentForm(user=request.user)

    return render(request, "booking/book_appointment.html",
                  {"appointment_form": form})


def get_available_times(request):
    """
    Return available time slots for a selected date
    """
    selected_date = request.GET.get("day")
    if not selected_date:
        # Returns error if no date is passed from the client
        return JsonResponse({"error": "No date provided"}, status=400)

    selected_date = parse_date(selected_date)
    all_times = [t[0] for t in TIME_CHOICES]

    # Gets already-booked times for that day
    booked_times = Appointment.objects.filter(day=selected_date).values_list(
        "time", flat=True
    )

    # Excludes booked times to only get available options
    available_times = [t for t in all_times if t not in booked_times]

    # Returns remaining time slots
    return JsonResponse({"available_times": available_times})


def get_fully_booked_dates(request):
    """
    Returns a list of dates that are fully booked the next 30 days
    """
    today = datetime.date.today()
    next_30_days = [today + datetime.timedelta(days=i) for i in range(30)]
    fully_booked = []

    for day in next_30_days:
        # Gets all booked time slots for this date
        booked_times = Appointment.objects.filter(day=day).values_list(
            "time", flat=True
        )

        # If all available times are booked the date is marked as full
        if len(booked_times) >= len(TIME_CHOICES):
            fully_booked.append(day.isoformat())

    # Returns list of fully booked dates
    return JsonResponse({"fully_booked_dates": fully_booked})


@login_required
def appointment_success(request):
    """
    Display confirmation page after successful booking
    Shows the latest booking for the logged in user
    """
    # Gets the latest appointment for the user
    latest_appointment = (
        Appointment.objects.filter(user=request.user).order_by("-booked_on").first()    # noqa
    )

    # Render success page with appointment details
    return render(
        request, "booking/appointment_success.html",
        {"appointment": latest_appointment}
    )


@login_required
def update_appointment(request, pk):
    """
    Allows logged in users to update or delete their existing appointment
    Only accessible to the user who created the appointment
    """
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)

    if request.method == "POST":
        # Appointment cancellation
        if "delete" in request.POST:
            appointment.delete()
            messages.success(request, "Appointment canceled.")
            return redirect("my_appointments")

        # Appointment update
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment updated.")
            return redirect("appointment_success")
    else:
        form = AppointmentForm(instance=appointment)

    return render(
        request,
        "booking/update_appointment.html",
        {"appointment_form": form, "appointment": appointment},
    )


@login_required
def my_appointments(request):
    """
    Displays all upcoming and past appointments for the logged-in user
    Ordered by date and time
    """
    appointments = Appointment.objects.filter(user=request.user).order_by("day", "time")    # noqa

    today = datetime.date.today()
    upcoming_appointments = appointments.filter(day__gte=today)

    return render(
        request,
        "booking/my_appointments.html",
        {
            "appointments": appointments,
            "upcoming_appointments": upcoming_appointments,
        },
    )
