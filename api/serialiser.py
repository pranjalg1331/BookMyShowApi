from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Museum, Slot, Ticket

class MuseumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museum
        fields = '__all__'

class SlotSerializer(serializers.ModelSerializer):
    remaining_seats = serializers.SerializerMethodField()
    class Meta:
        model = Slot
        fields = '__all__'
    def get_remaining_seats(self, obj):
        total_booked = obj.tickets.count()
        remaining_seats = obj.seat_limit - total_booked
        return remaining_seats


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Ticket
        fields = '__all__'
