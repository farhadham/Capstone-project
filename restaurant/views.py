from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer


def index(request):
    return render(request, 'index.html', {})


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated, ]
