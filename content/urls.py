from django.urls import path
from .views import get_page_content

urlpatterns = [
    path('pages/<str:page_slug>/', get_page_content, name='page_content_detail'),
    path('pages/', get_page_content, name='page_content_default'),
]
