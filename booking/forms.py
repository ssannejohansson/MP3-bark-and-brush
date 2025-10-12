from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'dog_name', 'dog_breed', 'service', 'day', 'time']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'}),
        }


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
