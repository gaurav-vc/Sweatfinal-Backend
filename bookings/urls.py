from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import submit_public_booking, CMSBookingLeadViewSet

router = DefaultRouter()
router.register(r'leads', CMSBookingLeadViewSet, basename='cms_leads')

urlpatterns = [
    path('', submit_public_booking, name='submit_public_booking'),
    path('cms/', include(router.urls)),
]
