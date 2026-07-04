from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_filter = ("price_per_night", 'room_type')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['room', 'guest_first_name', 'check_in_date', 'check_out_date', 'status']
    list_editable = ['status']
    list_filter = ['status']