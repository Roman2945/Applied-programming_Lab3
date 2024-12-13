from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:id>/', views.booking_detail, name='booking_detail'),
    path('bookings/create/', views.create_booking, name='create_booking'),
    path('bookings/<int:id>/edit/', views.edit_booking, name='edit_booking'),
    path('bookings/<int:id>/delete/', views.delete_booking, name='delete_booking'),

    path('airplanes/', views.airplane_list, name='airplane_list'),
    path('airplanes/create/', views.create_airplane, name='create_airplane'),
    path('airplanes/<int:id>/delete/', views.delete_airplane, name='delete_airplane'),
]




