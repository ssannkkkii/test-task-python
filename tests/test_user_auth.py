import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    response = client.post(reverse('register'), {
        "email": "new@example.com",
        "full_name": "New User",
        "password": "newpassword123"
    })
    assert response.status_code == 201
    assert "email" in response.data

@pytest.mark.django_db
def test_token_obtain(create_user):
    user = create_user()
    client = APIClient()
    response = client.post(reverse('token_obtain_pair'), {
        "email": user.email,
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access" in response.data
