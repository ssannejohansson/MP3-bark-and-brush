from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
from .models import Appointment
from .forms import AdminAppointmentForm


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """
    Custom admin interface for Appointment Model
    """

    form = AdminAppointmentForm
    list_display = ("user", "service", "size", "day", "time", "booked_on")
    list_filter = ("day", "time", "service")
    search_fields = ("user__username", "service", "user__email")
    ordering = ("day", "time")

    def get_changeform_initial_data(self, request):
        """
        Pre-fills today's date when adding a new appointment
        """
        from datetime import date

        return {"day": date.today()}

    def save_model(self, request, obj, form, change):
        """
        Prevents saving duplicate appointments for the same day and time
        """
        if not change or form.has_changed():
            if (
                Appointment.objects.filter(day=obj.day, time=obj.time)
                .exclude(pk=obj.pk)
                .exists()
            ):
                raise ValidationError(
                    f"This time slot on {obj.day}at {obj.time} is already booked."  # noqa
                )
        super().save_model(request, obj, form, change)
