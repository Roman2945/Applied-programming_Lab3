from django.shortcuts import render, get_object_or_404, redirect
from BookingApp.models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['passenger', 'status', 'starting_station', 'ending_station', 'train_journey', 'seat']


def objects_list(request):
    objects = Booking.objects.all()
    return render(request, 'templates_app/booking_list.html', {'objects': objects})


def booking_detail(request, id):
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'templates_app/booking_detail.html', {'booking': booking})


def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objects_list')
    else:
        form = BookingForm()
    return render(request, 'templates_app/create_booking.html', {'form': form})


def edit_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('objects_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'templates_app/edit_booking.html', {'form': form, 'booking': booking})


def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        booking.delete()
        return redirect('objects_list')
    return render(request, 'templates_app/booking_detail.html', {'booking': booking})
