from django.urls import path
from . import views

urlpatterns = [
    path('objects/', views.objects_list, name='objects_list'),
    path('bookings/<int:id>/', views.booking_detail, name='booking_detail'),
    path('bookings/create/', views.create_booking, name='create_booking'),
    path('bookings/<int:id>/edit/', views.edit_booking, name='edit_booking'),
    path('bookings/<int:id>/delete/', views.delete_booking, name='delete_booking'),
]
