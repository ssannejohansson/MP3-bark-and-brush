from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import * 
from django.contrib import messages

# Create your views here.

"""
Renders the template of booking.html
"""


def booking(request):
    return render(request, "booking.html", {})