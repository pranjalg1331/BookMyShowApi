# museum/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MuseumViewSet, SlotViewSet, TicketViewSet,MuseumSlotListView

router = DefaultRouter()
router.register(r'museums', MuseumViewSet)
router.register(r'slots', SlotViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('museums/<str:museum_name>/slots/', MuseumSlotListView.as_view(), name='slots-by-museum-name'),
]
