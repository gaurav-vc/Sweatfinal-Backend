from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.models import User
from .serializers import UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_initial_admin(request):
    """Utility to register initial admin if none exists."""
    if User.objects.filter(is_superuser=True).exists():
        return Response({'message': 'Admin already initialized'}, status=status.HTTP_400_BAD_REQUEST)
    
    username = request.data.get('username', 'admin')
    password = request.data.get('password', 'Admin@1234')
    email = request.data.get('email', 'admin@sweathq.in')
    
    user = User.objects.create_superuser(username=username, email=email, password=password)
    return Response({'message': 'Superuser created successfully', 'username': username}, status=status.HTTP_201_CREATED)
