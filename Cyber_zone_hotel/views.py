from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from . models import Room, Booking, User
from .forms import CustomUserCreationForm, BookingForm
from django.contrib.auth import login

def room_list(request):
    rooms = Room.objects.all()
    type = request.GET.get("type")
    max_price = request.GET.get("max_price")

    if type:
        rooms = Room.objects.filter(room_type=type)
    if max_price:
        rooms = rooms.filter(price_per_night__lte=max_price)

    return render(request, 'room_list.html', {"rooms": rooms})


def room_detail(request, id):
    room = get_object_or_404(Room, id=id)
    return render(request, "room_detail.html", {"room":room})


@login_required
def book_room(request, id):
    room = get_object_or_404(Room, id=id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.status = 'pending'
            booking.save()
            return redirect('room_list')
    else:
        form = BookingForm()
    return render(request, 'book_room.html', {'form': form})


def reg(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('room_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})