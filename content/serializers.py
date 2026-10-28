from rest_framework import serializers
from .models import (
    HeroBanner, Program, CelebrityVideo, Transformation,
    Coach, MembershipTier, FAQItem, ShopProduct, UploadedMedia
)

def extract_media_path(val):
    if not val:
        return None
    val_str = str(val).strip()
    if '/media/' in val_str:
        return val_str.split('/media/')[-1]
    if val_str.startswith('http://') or val_str.startswith('https://'):
        return val_str.split('/')[-1]
    return val_str


class FlexibleFileField(serializers.FileField):
    def to_internal_value(self, data):
        if isinstance(data, str):
            clean = extract_media_path(data)
            return clean if clean else None
        return super().to_internal_value(data)

    def to_representation(self, value):
        if not value:
            return None
        request = self.context.get('request')
        try:
            name = str(value.name if hasattr(value, 'name') else value).lstrip('/')
            if name.startswith('http://') or name.startswith('https://'):
                return name
            path = f"/media/{name}"
            return request.build_absolute_uri(path) if request else f"http://localhost:8000{path}"
        except Exception:
            return f"http://localhost:8000/media/{value}"


class FlexibleImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str):
            clean = extract_media_path(data)
            return clean if clean else None
        return super().to_internal_value(data)

    def to_representation(self, value):
        if not value:
            return None
        request = self.context.get('request')
        try:
            name = str(value.name if hasattr(value, 'name') else value).lstrip('/')
            if name.startswith('http://') or name.startswith('https://'):
                return name
            path = f"/media/{name}"
            return request.build_absolute_uri(path) if request else f"http://localhost:8000{path}"
        except Exception:
            return f"http://localhost:8000/media/{value}"


class HeroBannerSerializer(serializers.ModelSerializer):
    video_file = FlexibleFileField(required=False, allow_null=True)
    fallback_image = FlexibleImageField(required=False, allow_null=True)
    video_url = serializers.SerializerMethodField()
    background_image = serializers.SerializerMethodField()

    class Meta:
        model = HeroBanner
        fields = '__all__'
        extra_kwargs = {
            'eyebrow': {'required': False, 'allow_blank': True},
            'headline': {'required': False, 'allow_blank': True},
            'highlight_text': {'required': False, 'allow_blank': True},
            'subheading': {'required': False, 'allow_blank': True},
            'cta_primary_text': {'required': False, 'allow_blank': True},
            'cta_primary_link': {'required': False, 'allow_blank': True},
            'cta_secondary_text': {'required': False, 'allow_blank': True},
            'cta_secondary_link': {'required': False, 'allow_blank': True},
        }

    def get_video_url(self, obj):
        request = self.context.get('request')
        if obj.video_file:
            try:
                name = str(obj.video_file.name).lstrip('/')
                if name.startswith('http://') or name.startswith('https://'):
                    return name
                path = f"/media/{name}"
                return request.build_absolute_uri(path) if request else f"http://localhost:8000{path}"
            except Exception:
                return f"http://localhost:8000/media/{obj.video_file}"
        return None

    def get_background_image(self, obj):
        request = self.context.get('request')
        if obj.fallback_image:
            try:
                name = str(obj.fallback_image.name).lstrip('/')
                if name.startswith('http://') or name.startswith('https://'):
                    return name
                path = f"/media/{name}"
                return request.build_absolute_uri(path) if request else f"http://localhost:8000{path}"
            except Exception:
                return f"http://localhost:8000/media/{obj.fallback_image}"
        return None

    def create(self, validated_data):
        raw_video = self.initial_data.get('video_url') or self.initial_data.get('video_file')
        raw_image = self.initial_data.get('background_image') or self.initial_data.get('fallback_image')
        if raw_video and not validated_data.get('video_file'):
            validated_data['video_file'] = extract_media_path(raw_video)
        if raw_image and not validated_data.get('fallback_image'):
            validated_data['fallback_image'] = extract_media_path(raw_image)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'video_url' in self.initial_data or 'video_file' in self.initial_data:
            raw_video = self.initial_data.get('video_url')
            if not raw_video:
                raw_video = self.initial_data.get('video_file')
            validated_data['video_file'] = extract_media_path(raw_video) if raw_video else None
        if 'background_image' in self.initial_data or 'fallback_image' in self.initial_data:
            raw_image = self.initial_data.get('background_image')
            if not raw_image:
                raw_image = self.initial_data.get('fallback_image')
            validated_data['fallback_image'] = extract_media_path(raw_image) if raw_image else None
        return super().update(instance, validated_data)


class ProgramSerializer(serializers.ModelSerializer):
    hero_image = FlexibleImageField(required=False, allow_null=True)
    featured_video = FlexibleFileField(required=False, allow_null=True)

    class Meta:
        model = Program
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'hero_image' in self.initial_data:
            val = self.initial_data.get('hero_image')
            validated_data['hero_image'] = extract_media_path(val) if val else None
        if 'featured_video' in self.initial_data:
            val = self.initial_data.get('featured_video')
            validated_data['featured_video'] = extract_media_path(val) if val else None
        return super().update(instance, validated_data)


class CelebrityVideoSerializer(serializers.ModelSerializer):
    video_file = FlexibleFileField(required=False, allow_null=True)
    thumbnail = FlexibleImageField(required=False, allow_null=True)

    class Meta:
        model = CelebrityVideo
        fields = '__all__'
        extra_kwargs = {
            'video_url': {'required': False, 'allow_blank': True, 'allow_null': True},
        }

    def update(self, instance, validated_data):
        if 'video_file' in self.initial_data:
            val = self.initial_data.get('video_file')
            validated_data['video_file'] = extract_media_path(val) if val else None
        if 'video_url' in self.initial_data:
            validated_data['video_url'] = self.initial_data.get('video_url') or None
        return super().update(instance, validated_data)


class TransformationSerializer(serializers.ModelSerializer):
    before_image = FlexibleImageField(required=False, allow_null=True)
    after_image = FlexibleImageField(required=False, allow_null=True)

    class Meta:
        model = Transformation
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'before_image' in self.initial_data:
            val = self.initial_data.get('before_image')
            validated_data['before_image'] = extract_media_path(val) if val else None
        if 'after_image' in self.initial_data:
            val = self.initial_data.get('after_image')
            validated_data['after_image'] = extract_media_path(val) if val else None
        if 'before_image_url' in self.initial_data:
            validated_data['before_image_url'] = self.initial_data.get('before_image_url') or ''
        if 'after_image_url' in self.initial_data:
            validated_data['after_image_url'] = self.initial_data.get('after_image_url') or ''
        return super().update(instance, validated_data)


class CoachSerializer(serializers.ModelSerializer):
    photo = FlexibleImageField(required=False, allow_null=True)
    image = FlexibleImageField(required=False, allow_null=True)

    class Meta:
        model = Coach
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'photo' in self.initial_data:
            val = self.initial_data.get('photo')
            validated_data['photo'] = extract_media_path(val) if val else None
        if 'photo_url' in self.initial_data:
            validated_data['photo_url'] = self.initial_data.get('photo_url') or ''
        return super().update(instance, validated_data)


class MembershipTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipTier
        fields = '__all__'


class FAQItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQItem
        fields = '__all__'


class ShopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopProduct
        fields = '__all__'


class UploadedMediaSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = UploadedMedia
        fields = ['id', 'title', 'media_type', 'file', 'file_url', 'tags', 'uploaded_at']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and hasattr(obj.file, 'url'):
            if request:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url
        return None
