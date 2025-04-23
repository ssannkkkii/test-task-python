import pytest
from rest_framework.test import APIClient
from restaurant.models import Restaurant, Menu
from datetime import date

@pytest.mark.django_db
def test_vote(create_user):
    user = create_user(is_employee=True)
    client = APIClient()
    client.force_authenticate(user)

    restaurant = Restaurant.objects.create(name="Place", created_by=user)
    menu = Menu.objects.create(restaurant=restaurant, date=date.today(), description="Food")

    res = client.post("/votes/", {
        "menu": menu.id
    })

    assert res.status_code == 201
    assert user.votes.count() == 1

@pytest.mark.django_db
def test_results_today(create_user):
    user = create_user(is_employee=True)
    client = APIClient()
    client.force_authenticate(user)

    restaurant = Restaurant.objects.create(name="VotePlace", created_by=user)
    menu = Menu.objects.create(restaurant=restaurant, date=date.today(), description="Dishes")

    client.post("/votes/", {"menu": menu.id})
    res = client.get("/votes/results_today/")

    assert res.status_code == 200
    assert len(res.data) > 0
