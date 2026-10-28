from django.urls import path
from .views import get_page_content

urlpatterns = [
    path('content/<str:page_slug>/', get_page_content, name='public_page_content'),
    path('content/', get_page_content, {'page_slug': 'home'}, name='public_home_content'),
]
