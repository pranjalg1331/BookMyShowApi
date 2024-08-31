from django.contrib import admin
from .models import Museum, Slot, Ticket

@admin.register(Museum)
class MuseumAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description')
    search_fields = ('name', 'address')

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('museum', 'start_time', 'end_time', 'seat_limit')
    list_filter = ('museum', 'start_time', 'end_time')
    search_fields = ('museum__name',)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('slot', 'user', 'booked_at')
    list_filter = ('slot', 'user', 'booked_at')
    search_fields = ('user__username', 'slot__museum__name')