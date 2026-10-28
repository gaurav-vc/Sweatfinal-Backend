from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CMSHeroViewSet, CMSProgramViewSet, CMSCelebrityViewSet,
    CMSTransformationViewSet, CMSCoachViewSet, CMSMembershipViewSet,
    CMSShopViewSet, CMSMediaViewSet, upload_media_direct
)

router = DefaultRouter()
router.register(r'heroes', CMSHeroViewSet, basename='cms_heroes')
router.register(r'programs', CMSProgramViewSet, basename='cms_programs')
router.register(r'celebrities', CMSCelebrityViewSet, basename='cms_celebrities')
router.register(r'transformations', CMSTransformationViewSet, basename='cms_transformations')
router.register(r'coaches', CMSCoachViewSet, basename='cms_coaches')
router.register(r'memberships', CMSMembershipViewSet, basename='cms_memberships')
router.register(r'shop', CMSShopViewSet, basename='cms_shop')
router.register(r'media', CMSMediaViewSet, basename='cms_media')

urlpatterns = [
    path('media/upload/', upload_media_direct, name='cms_media_upload_direct'),
    path('', include(router.urls)),
]
