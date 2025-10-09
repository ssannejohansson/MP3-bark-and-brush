from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Appointment
from django.contrib import messages


# Create your views here.

# Renders the template of booking.html
def booking(request):
    return render(request, "booking.html", {})


def book_appointment(request):
    # calls 'validWeekday' function to loop days you want in the next 31 days
    weekdays = validWeekday(32)

    # only show the days that are not fully booked
    validateWeekdays = isWeekdayValid(weekdays)

    """
    If the user submits the form correctly, it grabs the service and day value 
    from the submitted data. If no service is selected, the user gets a 
    message and is sent back to the booking page.
    """
    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service is None:
            messages.success(request, "Please select a service")
            return redirect('booking')
        
        # store day and service in django session
        request.session['day'] = day
        request.session['service'] = service

        return redirect('booking')
    
    return render(request, 'booking.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
    })


def bookingSubmit(request):
    user = request.user
    times = ["9:00 AM", "10:30 AM", "1:00 PM", "2:30 PM", "4:00 PM", "5:30 PM"]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=31)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    # get stored data from django session in book_appointment
    day = request.session.get('day')
    service = request.session.get('service')

    # only show the time of the day that has not been selected before (?)
    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

# --- comment to self: remove some of the if statements?
        if service != None:
            if day <= maxDate and day <= minDate:
                if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday':
                    if Appointment.objects.filter(day=day).count() < 7:
                        if Appointment.objects.filter(day=day, time=time).count() < 1:
                            AppointmentForm = Appointment.object.get_or_create(
                                user=user,
                                service=service,
                                day=day,
                                time=time,
                            )
                            messages.success(request, "Appointment Saved!")
                            return redirect('booking')
                    else:
                        messages.success(request,
                                         "The selected time is unavailable")
                else:
                    messages.success(request,
                                     "The selected day is full")
            else:
                messages.success(request,
                                 "The selected date isn't the "
                                 "in the correct time period")
        else: 
            messages.success(request, 
                             "Please select a service")
    
    return render(request, 'booking.html', {
        'times': hour,
    })


def userPanel (request):
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by('day', 'time')
    return render(request, 'userPanel.html', {
        'user':user,
        'appointments':appointments,
    })


def userUpdate(request, id):
    appointment = Appointment.objects.get(pk=id)
    userdatepicked = appointment.day

    # copy booking
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    # 24h if statement in template (?)
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    
    # calling 'validWeekday' function to loop days you want in 
    # the next 31 days
    weekdays = validWeekday(32)

    # only show the days that are not full
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')

        # store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service

        return redirect('userUpdateSubmit', id=id)

    return render(request, 'userUpdate.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
            'delta24': delta24,
            'id': id,
        })


def userUpdateSubmit(request, id):
    user = request.user
    times = ["9:00 AM", "10:30 AM", "1:00 PM", "2:30 PM", "4:00 PM", "5:30 PM"]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')

    # only show the time of the day that has not been selected
    # before and the time that should be edited
    hour = checkEditTime(times, day, id)
    appointment = Appointment.objects.get(pk=id)
    userSelectedTime = appointment.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday':
                    if Appointment.objects.filter(day=day).count() < 7:
                        if Appointment.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                            AppointmentForm = Appointment.objects.filter(pk=id).update(
                                user=user,
                                service=service,
                                day=day,
                                time=time,
                            ) 
                            messages.success(request, "Appointment edited")
                            return redirect('booking')
                        else:
                            messages.success(request, "The selected time has been reserved before")
                    else:
                        messages.success(request, "The selected day is full")
                else:
                    messages.success(request, "the selected date is incorrect")
            else:
                    messages.success(request, "The selected date isn't in the correct time period")
        else:
            messages.success(request, "Please select a service!")
        return redirect('userPanel')

    return render(request, 'userUpdateSubmit.html', {
        'times': hour,
        'id': id,
    })


def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=31)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    # only show the Appointments 31 days from today
    items = Appointment.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')


def dayToWeekday(x):
    """
    Parses the date string, x, into a Python datetime object.
    Converts the datetime object z into the full weekday name
    and returns the weekday name. 
    """
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    """
    Loop days you want in the next 31 days

    **Context**

    ``today``
    Gets the current date and time

    ``weekdays``
    Creates an empty list to store valid weekday dates

    ``for i in range(0, days) loop``
    Loops through each day from today up to the next days.
    Adds i days to today to get each future date.
    Formats the date x into the weekday name.
    Checks if the day is a day that is bookable (Sat and sun is skipped
    since the groomer in this case is closed those days).
    Adds the valid weekday date as a formatted string to the weekday list.

    ``return weekdays```
    Returns list of weekdays.
    """
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Tuesday' or y == 'Wednesday' or y == 'Thursday' or y == 'Friday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays
        

def isWeekdayValid(x):
    """
    Checks the list of days from validWeekday to see if the days are fully
    booked. The maximum number of appointments in a day are 6 so it looks for
    days with < 6 booked appointments). Valid dates are stored in empty
    validateWeekdays list and are then returned.
    """
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 6:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    # only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x

def checkEditTime(times, day, id):
    # only show the time of the day that has not been selected before:
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x
