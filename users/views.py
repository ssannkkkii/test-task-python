from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import RegisterSerializer, BecomeEmployeeSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "email": user.email,
            "full_name": user.full_name,
            "is_staff": user.is_staff
        })

class BecomeEmployeeView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = BecomeEmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user