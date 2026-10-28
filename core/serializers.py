from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AdminProfile

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'role']

    def get_role(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.role
        return 'Administrator'
