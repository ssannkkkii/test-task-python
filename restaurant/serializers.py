from rest_framework import serializers
from .models import Restaurant, Menu, MenuItem, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'is_vegetarian']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'date', 'description']


class MenuWithItemsSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    items = MenuItemSerializer(many=True)

    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'date', 'description', 'items']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'menu', 'voted_at']
        read_only_fields = ['user', 'voted_at']
