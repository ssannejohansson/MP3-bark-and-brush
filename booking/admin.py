from django.contrib import admin
from .models import Appointment
from .forms import AdminAppointmentForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    form = AdminAppointmentForm
    list_display = ('user', 'service', 'size', 'day', 'time', 'booked_on')
    list_filter = ('day', 'time', 'service')
    search_fields = ('user__username', 'service', 'user_email')
    ordering = ('day', 'time')

    # pre-fill today's date when adding
    def get_changeform_initial_data(self, request):
        from datetime import date
        return {'day': date.today()}
    
     #  prevent saving a duplicate appointment
    def save_model(self, request, obj, form, change):
        # Only check for duplicates if it's a new appointment or the time/day/user has changed
        if not change or form.has_changed():
            if Appointment.objects.filter(day=obj.day, time=obj.time).exclude(pk=obj.pk).exists():
                from django.core.exceptions import ValidationError
                raise ValidationError(f'This time slot on {obj.day} at {obj.time} is already booked.')
        super().save_model(request, obj, form, change)