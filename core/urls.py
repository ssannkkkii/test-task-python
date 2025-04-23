from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurant.views import (
    RestaurantViewSet,
    MenuViewSet,
    VoteViewSet
)
from users.views import (
    RegisterView,
    ProfileView,
    BecomeEmployeeView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')
router.register(r'menus', MenuViewSet, basename='menu')
router.register(r'votes', VoteViewSet, basename='vote')

urlpatterns = [
    path('', include(router.urls)),

    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
    path('auth/become-employee/', BecomeEmployeeView.as_view(), name='become-employee'),
]
