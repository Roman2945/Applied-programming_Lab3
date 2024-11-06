from .models import Booking
from django.db.models import Count


class BookingRepository:
    @staticmethod
    def get_all_bookings():
        return Booking.objects.all()

    @staticmethod
    def get_booking_by_id(booking_id):
        return Booking.objects.get(id=booking_id)

    @staticmethod
    def create_booking(data):
        return Booking.objects.create(**data)

    @staticmethod
    def update_booking(booking, data):
        for field, value in data.items():
            setattr(booking, field, value)
        booking.save()
        return booking

    @staticmethod
    def delete_booking(booking):
        booking.delete()


class ReportRepository:
    @staticmethod
    def get_booking_summary():
        return Booking.objects.values('status__status_name').annotate(total=Count('id'))
