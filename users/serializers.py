from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'password')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class BecomeEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('is_employee',)
        read_only_fields = ('email',)

    def update(self, instance, validated_data):
        instance.is_employee = True
        instance.save()
        return instance