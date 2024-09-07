from rest_framework import viewsets
from .models import Museum, Slot, Ticket
from .serialiser import MuseumSerializer, SlotSerializer, TicketSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Slot
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import generics

class MuseumSlotListView(generics.ListAPIView):
    serializer_class = SlotSerializer
    def get_queryset(self):
        museum_name = self.kwargs['museum_name']
        return Slot.objects.filter(museum__name=museum_name)

class MuseumViewSet(viewsets.ModelViewSet):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer

class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
    
    @action(detail=True, methods=['get'])
    def remaining_seats(self, request, pk=None):
        slot = self.get_object()
        total_booked_seats = sum(ticket.seats_booked for ticket in slot.tickets.all())
        remaining_seats = slot.available_seats - total_booked_seats
        return Response({'remaining_seats': remaining_seats})

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# class SlotViewSet(viewsets.ModelViewSet):
#     queryset = Slot.objects.all()
#     serializer_class = SlotSerializer

   