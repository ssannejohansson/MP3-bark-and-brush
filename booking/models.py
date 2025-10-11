from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
# Variable for the choices of service the user can book
SERVICE_CHOICES = (
    ("Full Groom", "Full Groom"),
    ("Bath and Tidy", "Bath and Tidy"),
    ("The De-shedding Package", "The De-shedding Package"),
    ("The Paw Package", "The Paw Package"),
)

# Variable of times available for booking
TIME_CHOICES = (
    ("9:00 AM", "9:00 AM"),
    ("10:30 AM", "10:30 AM"),
    ("1:00 PM", "1:00 PM"),
    ("2:30 PM", "2:30 PM"),
    ("4:00 PM", "4:00 PM"),
    ("5:30 PM", "5:30 PM"),
)


class Appointment(models.Model):
    """
    ``user``
    When a user delete its account, all its appointments will be
    deleted. Null and blank set to false ensures that every booking
    needs to be associated with a user.

    ``service``
    Charfield with max_length set to tell the database how much space
    to reserve for the field even though specified choices are given.
    Choices are defined in the SERVICE_CHOICES variable above with full
    groom as its default choice.

    ``day/time``
    Selection of date and time for booking an appointment. Default set
    to default = datetime.now to set default to todays date and time.

        ``booked_on```
    Keeps track of then the appointment was booked. Blank set to
    false to ensure the field is not left blank.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                             blank=False)
    service = models.CharField(max_length=30, choices=SERVICE_CHOICES,
                               default="Full Groom")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES,
                            default="9:00 AM")
    booked_on = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
