from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',          # Auto-generated primary key
            'book_name',
            'author',
            'name',
            'address',
            'phone_no',
            'quantity',
            'payment_method'
        ]