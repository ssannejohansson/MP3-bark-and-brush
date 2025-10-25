from datetime import date
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from crispy_forms.bootstrap import StrictButton
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    """
    Form for booking appointments
    """

    class Meta:
        model = Appointment
        fields = [
            "name",
            "email",
            "dog_name",
            "dog_breed",
            "service",
            "size",
            "day",
            "time",
        ]
        widgets = {
            "day": forms.DateInput(attrs={"type": "date"}),
        }

        error_messages = {
            "email":
            {"required": "We need your email to confirm your appointment."},
            "dog_name": {"required": "Please tell us your dog's name."},
            "dog_breed": {"required": "Let us know your dog's breed."},
            "service": {"required": "Please select a service."},
            "size": {"required": "Please choose your dog's size."},
            "day": {"required": "Pick a preferred date for your appointment."},
            "time": {"required": "Select a suitable time slot."},
        }

    def __init__(self, *args, **kwargs):
        # Catch the user from the view
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        # Prevent selecting past dates
        self.fields["day"].widget.attrs["min"] = date.today().isoformat()

        # Auto-fills name and email based on the users information
        if user and user.is_authenticated:
            self.fields["name"].initial = f"{user.first_name}".strip()
            self.fields["email"].initial = user.email

        # Add disabled placeholder option to dropdowns
        for field_name, placeholder in {
            "service": "Select a service...",
            "size": "Select your dog's size...",
            "day": "Select a day...",
            "time": "Select a time...",
        }.items():
            field = self.fields.get(field_name)

            if field and hasattr(field, "choices") and field.choices:
                choices = list(field.choices)
                # Prepend the placeholder as the first choice
                field.choices = [("", placeholder)] + choices
                # Make the placeholder selected by default
                field.initial = ""
                # Keep required validation
                field.widget.attrs.update({"required": "required"})

        # Crispy form setup
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "booking-form"
        self.helper.attrs = {'novalidate': ''}

        # Crispy layout
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-6"),
                Column("email", css_class="col-md-6"),
            ),
            Row(
                Column("dog_name", css_class="col-md-6"),
                Column("dog_breed", css_class="col-md-6"),
            ),
            Row(
                Column("service", css_class="col-md-6"),
                Column("size", css_class="col-md-6"),
            ),
            HTML(
                '<div class="text-start mb-3">'
                '  <a href="{% url "services" %}" target="_blank" class="small text-muted">'    # noqa
                "    Need to refresh your memory? See our services here!"
                "  </a>"
                "</div>"
            ),
            Row(
                Column("day", css_class="col-md-6"),
                Column("time", css_class="col-md-6"),
            ),
            StrictButton(
                'Book Appointment<i class="fa-solid fa-calendar ms-2"></i>',
                "book-appointment",
                type="submit",
                css_class="custom-btn-booking",
            ),
        )


class AdminAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        day = cleaned_data.get("day")
        time = cleaned_data.get("time")

        if day and time:
            # Prevent double-booking (excluding current instance)
            qs = Appointment.objects.filter(day=day, time=time)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise forms.ValidationError
            ("This time slot is already booked.")

        return cleaned_data
