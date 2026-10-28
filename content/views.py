from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .models import (
    HeroBanner, Program, CelebrityVideo, Transformation,
    Coach, MembershipTier, FAQItem, ShopProduct, UploadedMedia
)
from .serializers import (
    HeroBannerSerializer, ProgramSerializer, CelebrityVideoSerializer,
    TransformationSerializer, CoachSerializer, MembershipTierSerializer,
    FAQItemSerializer, ShopProductSerializer, UploadedMediaSerializer
)

import os

# -------------------------------------------------------------
# PUBLIC CONTENT VIEWS (READ-ONLY FOR REACT FRONTEND)
# -------------------------------------------------------------
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_page_content(request, page_slug='home'):
    """Returns aggregated content package tailored to the requested page slug."""
    hero = HeroBanner.objects.filter(page_identifier=page_slug, is_active=True).first()
    if not hero:
        hero = HeroBanner.objects.filter(page_identifier='home', is_active=True).first()

    # If hero exists but video_file is not set, auto-link any uploaded video for this page
    if hero and not hero.video_file:
        uploaded_v = UploadedMedia.objects.filter(
            media_type='video',
            title__icontains=f"{page_slug}_hero"
        ).order_by('-uploaded_at').first()
        if not uploaded_v and page_slug == 'home':
            uploaded_v = UploadedMedia.objects.filter(media_type='video').order_by('-uploaded_at').first()
        if uploaded_v and uploaded_v.file:
            hero.video_file = uploaded_v.file.name
            hero.save(update_fields=['video_file'])

    program = Program.objects.filter(slug=page_slug, is_active=True).first()

    data = {
        'page': page_slug,
        'hero': HeroBannerSerializer(hero, context={'request': request}).data if hero else None,
        'program': ProgramSerializer(program, context={'request': request}).data if program else None,
        'programs': ProgramSerializer(Program.objects.filter(is_active=True), many=True, context={'request': request}).data,
        'celebrities': CelebrityVideoSerializer(CelebrityVideo.objects.filter(is_active=True), many=True, context={'request': request}).data,
        'transformations': TransformationSerializer(Transformation.objects.filter(is_active=True), many=True, context={'request': request}).data,
        'coaches': CoachSerializer(Coach.objects.filter(is_active=True), many=True, context={'request': request}).data,
        'memberships': MembershipTierSerializer(MembershipTier.objects.all(), many=True, context={'request': request}).data,
        'faqs': FAQItemSerializer(FAQItem.objects.filter(page_category=page_slug), many=True, context={'request': request}).data or FAQItemSerializer(FAQItem.objects.filter(page_category='home'), many=True, context={'request': request}).data,
        'products': ShopProductSerializer(ShopProduct.objects.filter(is_available=True), many=True, context={'request': request}).data,
    }
    return Response(data)


# -------------------------------------------------------------
# CMS ADMIN VIEWSETS (FULL CRUD FOR ADMIN STUDIO)
# -------------------------------------------------------------
class CMSHeroViewSet(viewsets.ModelViewSet):
    queryset = HeroBanner.objects.all()
    serializer_class = HeroBannerSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class CMSProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class CMSCelebrityViewSet(viewsets.ModelViewSet):
    queryset = CelebrityVideo.objects.all()
    serializer_class = CelebrityVideoSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class CMSTransformationViewSet(viewsets.ModelViewSet):
    queryset = Transformation.objects.all()
    serializer_class = TransformationSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class CMSCoachViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class CMSMembershipViewSet(viewsets.ModelViewSet):
    queryset = MembershipTier.objects.all()
    serializer_class = MembershipTierSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class CMSShopViewSet(viewsets.ModelViewSet):
    queryset = ShopProduct.objects.all()
    serializer_class = ShopProductSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class CMSMediaViewSet(viewsets.ModelViewSet):
    queryset = UploadedMedia.objects.all()
    serializer_class = UploadedMediaSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser]


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@parser_classes([MultiPartParser, FormParser])
def upload_media_direct(request):
    """Direct multi-part upload endpoint for CMS Studio drag-and-drop."""
    file_obj = request.FILES.get('file')
    if not file_obj:
        return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
    
    title = request.data.get('title', file_obj.name)
    tags = request.data.get('tags', '')
    content_type = getattr(file_obj, 'content_type', '') or ''
    ext = os.path.splitext(file_obj.name)[1].lower()
    is_video = 'video' in content_type or ext in ['.mp4', '.mov', '.webm', '.ogg', '.m4v', '.avi', '.mkv']
    media_type = 'video' if is_video else 'photo'
    
    media = UploadedMedia.objects.create(
        title=title,
        file=file_obj,
        media_type=media_type,
        tags=tags
    )
    serializer = UploadedMediaSerializer(media, context={'request': request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)
