import pytest
from rest_framework.test import APIClient
from restaurant.models import Restaurant, Menu
from django.urls import reverse
from datetime import date

@pytest.mark.django_db
def test_create_restaurant(create_user):
    user = create_user()
    client = APIClient()
    client.force_authenticate(user)

    res = client.post("/restaurants/", {
        "name": "KDE8",
        "address": "Main st 123",
        "phone": "123456"
    })
    assert res.status_code == 201
    assert Restaurant.objects.count() == 1

@pytest.mark.django_db
def test_create_menu(create_user):
    user = create_user()
    client = APIClient()
    client.force_authenticate(user)

    res = client.post("/restaurants/", {
        "name": "Testaurant"
    })
    restaurant_id = res.data["id"]

    menu_res = client.post("/menus/", {
        "restaurant": restaurant_id,
        "date": str(date.today()),
        "description": "Lunch"
    })

    assert menu_res.status_code == 201
    assert Menu.objects.count() == 1
