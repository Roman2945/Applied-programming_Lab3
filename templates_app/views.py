import requests
from django.shortcuts import render, get_object_or_404, redirect
from BookingApp.models import Booking
from BookingApp.forms import BookingForm
from templates_app.NetworkHelper import NetworkHelper




API_CONFIG = {
    'airplanes': {
        'base_url': 'http://127.0.0.1:8000/api/',
        'username': 'Roman',
        'password': 'Arty123123'
    }
}


def get_api_config(endpoint):
    """Отримання конфігурації для заданого ендпоінта."""
    return API_CONFIG.get(endpoint, {})

def get_auth_token(endpoint):
    """Отримання токена для доступу до REST API."""
    config = get_api_config(endpoint)
    try:
        return NetworkHelper.get_auth_token(config['base_url'], config['username'], config['password'])
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            raise ValueError("Invalid credentials for API access. Please verify API_CONFIG.")
        raise

# =======================
# Views для Airplanes
# =======================

def create_airplane(request):
    """Створюємо новий літак через REST API."""
    if request.method == 'POST':
        token = get_auth_token('airplanes')
        config = get_api_config('airplanes')
        data = {
            'model': request.POST.get('model'),
            'capacity': request.POST.get('capacity'),
            'manufacturer': request.POST.get('manufacturer'),
        }
        NetworkHelper.create_item(config['base_url'], 'airplanes', data, token)
        return redirect('airplane_list')
    return render(request, 'templates_app/create_airplane.html')



def airplane_list(request):
    """Отримуємо список літаків через REST API."""
    try:
        token = get_auth_token('airplanes')
        config = get_api_config('airplanes')
        airplanes = NetworkHelper.get_list(config['base_url'], 'airplanes', token)
        return render(request, 'templates_app/airplane_list.html', {'airplanes': airplanes})
    except Exception as e:
        return render(request, 'templates_app/airplane_list.html', {'error': str(e)})




def delete_airplane(request, id):
    """Видаляємо літак через REST API."""
    try:
        token = get_auth_token('airplanes')
        config = get_api_config('airplanes')
        NetworkHelper.delete_item(config['base_url'], 'airplanes', id, token)
        return redirect('airplane_list')
    except Exception as e:
        return render(request, 'templates_app/airplane_list.html', {'error': str(e)})




def booking_list(request):
    """Отримуємо список бронювань з локальної бази даних."""
    bookings = Booking.objects.all()
    return render(request, 'templates_app/booking_list.html', {'bookings': bookings})

def booking_detail(request, id):
    """Отримуємо деталі бронювання."""
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'templates_app/booking_detail.html', {'booking': booking})

def create_booking(request):
    """Створюємо нове бронювання."""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'templates_app/create_booking.html', {'form': form})

def edit_booking(request, id):
    """Редагуємо існуюче бронювання."""
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_detail', id=id)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'templates_app/edit_booking.html', {'form': form, 'booking': booking})

def delete_booking(request, id):
    """Видаляємо бронювання."""
    booking = get_object_or_404(Booking, id=id)
    booking.delete()
    return redirect('booking_list')
