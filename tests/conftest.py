import pytest
from django.contrib.auth import get_user_model

@pytest.fixture
def user_data():
    return {"email": "user@example.com", "password": "testpass123", "full_name": "Test User"}

@pytest.fixture
def create_user(db, user_data):
    def make_user(**kwargs):
        data = {**user_data, **kwargs}
        return get_user_model().objects.create_user(**data)
    return make_user
