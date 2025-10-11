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
    list_display = ('user', 'service', 'day', 'time', 'booked_on')
    list_filter = ('day', 'time', 'service')
    search_fields = ('user__username', 'service')

    # Optional: pre-fill today's date when adding
    def get_changeform_initial_data(self, request):
        from datetime import date
        return {'day': date.today()}