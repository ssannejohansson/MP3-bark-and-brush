from django import forms
from .models import Appointment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'dog_name', 'dog_breed', 'service', 'size', 'day', 'time']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'booking-form'

        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('email'),
            ),
            Row(
                Column('dog_name'),
                Column('dog_breed'),
            ),
            Row(
                Column('service'),
                Column('size'),
            ),
            Row(
                Column('day', css_class='col-md-6'),
                Column('time', css_class='col-md-6'),
            ),
            Submit('submit', 'Book Appointment')
        )


class AdminAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        day = cleaned_data.get('day')
        time = cleaned_data.get('time')

        if day and time:
            # Prevent double-booking (excluding current instance)
            qs = Appointment.objects.filter(day=day, time=time)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise forms.ValidationError("This time slot is already booked.")

        return cleaned_data
