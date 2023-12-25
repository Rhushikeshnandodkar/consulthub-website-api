from django.contrib import admin
from .models import *
# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ['consultent', 'booking_user', 'is_paid', 'time_slot']
admin.site.register(ConsultBooking, BookingAdmin)