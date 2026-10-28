from django.db import models
from django.contrib.auth.models import User

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=50, default='Super Admin')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
