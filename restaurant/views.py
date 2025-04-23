from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from django.db.models import Count
from datetime import date

from .models import Restaurant, Menu, MenuItem, Vote
from .serializers import (
    RestaurantSerializer, MenuSerializer,
    MenuItemSerializer, VoteSerializer, MenuWithItemsSerializer
)


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_employee


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list_today', 'retrieve_today']:
            return MenuWithItemsSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated])
    def list_today(self, request):
        today_menus = Menu.objects.filter(date=date.today()).prefetch_related("items", "restaurant")
        serializer = self.get_serializer(today_menus, many=True)
        return Response(serializer.data)


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated])
    def results_today(self, request):
        today_votes = Vote.objects.filter(menu__date=date.today())
        results = today_votes.values(
            'menu__restaurant__name'
        ).annotate(votes=Count('id')).order_by('-votes')
        return Response(results)
