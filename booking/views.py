from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import * 
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