from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now


# Create your views here.
@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.booked_on = now()
            appointment.save()
            return redirect('appointment_success')  # You can define this URL/view
    else:
        form = AppointmentForm()

    return render(request, 'booking/book_appointment.html', {'form': form})