from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    STATUS_CHOICES = [('available', 'Доступен'), ('occupied', 'Занят'), ('maintenance', 'На обслуживании')]
    ROOM_TYPE_CHOICES = [('double_room', 'Двухместный номер'), ('lux_room', 'Люкс комната'), ('single_room', 'Одноместный номер')]
    room_title = models.CharField(max_length=50)
    room_type = models.CharField(max_length=25, choices=ROOM_TYPE_CHOICES, default='single_room')
    price_per_night = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField(max_length=1000)
    image_main = models.ImageField(upload_to="room_images/")
    image_bathroom = models.ImageField(upload_to="room_images/", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.room_title

class Booking(models.Model):
    STATUS_CHOICES = [('pending', 'Ожидает'), ('confirmed', 'Подтверждено'), ('cancelled', 'Отменено'),]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests_count = models.PositiveSmallIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    guest_first_name = models.CharField(max_length=100)
    guest_phone = models.CharField(max_length=20, blank=True)
