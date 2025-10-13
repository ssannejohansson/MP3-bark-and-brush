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

SIZE_CHOICES = (
    ("Small (under 20 lbs)", "Small (under 20 lbs)"),
    ("Medium (20-50 lbs)", "Medium (20-50 lbs)"),
    ("Large (50-80 lbs)", "Large (50-80 lbs)"),
    ("Giant (over 80 lbs)", "Giant (over 80 lbs)"),
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

    ``name``
    Charfield with max_length set to 50 to tell the database how much space
    to reserve for the field.

    ``email``
    Emailfield with null and blank set to false, to make this fields
    required to fill in.

    ``dog_name and dog_breed``
    Charfield with max_length set to 50 tell the database how much space
    to reserve for the field. Dog_name with blank set to True to tell the
    database that this field can be left blank. Dog_breed with null and blank
    set to false to ensure the field is not left blank.

    ``service and size``
    Charfields with max_length set to tell the database how much space
    to reserve for the field even though specified choices are given.
    Choices are defined in the SERVICE_CHOICES and SIZE_CHOICES variables above
    with full groom and small as its default choices.

    ``day and time``
    Selection of date and time for booking an appointment. Default set
    to default = datetime.now to set default to todays date and time.

        ``booked_on```
    Keeps track of then the appointment was booked. Blank set to
    false to ensure the field is not left blank.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                             blank=False)
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(null=False, blank=False)
    dog_name = models.CharField(max_length=50, blank=True)
    dog_breed = models.CharField(max_length=50, null=False, blank=False)
    service = models.CharField(max_length=30, choices=SERVICE_CHOICES,
                               default="Full Groom")
    size = models.CharField(max_length=30, choices=SIZE_CHOICES,
                            default="Small (under 20 lbs)") 
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES,
                            default="9:00 AM")
    booked_on = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"{self.name} | day: {self.day} | time: {self.time}"


# prevents double booking
class Meta:
    unique_together = ('day', 'time')