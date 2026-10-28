from django.db import models

class HeroBanner(models.Model):
    page_identifier = models.CharField(max_length=50, unique=True, help_text="e.g. 'home', 'programs', 'bootcamp'")
    eyebrow = models.CharField(max_length=150, default="SWEAT HQ · Andheri · Entry by assessment")
    headline = models.CharField(max_length=255, default="WHERE THE STARS TRAIN. NOW IT'S YOU.")
    highlight_text = models.CharField(max_length=120, default="NOW IT'S YOU.")
    subheading = models.TextField(default="The coaches and team behind Bollywood's best-known bodies are now coaching Andheri. Stronger, leaner and surer of yourself, with the same system the stars trust.")
    video_file = models.FileField(upload_to="heroes/videos/", blank=True, null=True)
    fallback_image = models.ImageField(upload_to="heroes/images/", blank=True, null=True)
    cta_primary_text = models.CharField(max_length=60, default="Experience SWEAT")
    cta_primary_link = models.CharField(max_length=100, default="/book")
    cta_secondary_text = models.CharField(max_length=60, default="Fitness assessment")
    cta_secondary_link = models.CharField(max_length=100, default="/assessment")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hero - {self.page_identifier}"


class Program(models.Model):
    order = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, help_text="e.g. 'bootcamp', 'pilates', 'glutes'")
    number = models.CharField(max_length=10, default="01") # '01', '02'...
    name = models.CharField(max_length=100) # 'BOOTCAMP', 'PILATES'
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    level_tags = models.JSONField(default=list, blank=True) # ["Olympic Lifting", "Gymnastics", "DTP"]
    hero_image = models.ImageField(upload_to="programs/", blank=True, null=True)
    featured_video = models.FileField(upload_to="programs/videos/", blank=True, null=True)
    class_ratio = models.CharField(max_length=100, default="2 coaches on the floor · capped at 16")
    duration = models.CharField(max_length=50, default="55 Mins")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'number']

    def __str__(self):
        return f"{self.number} - {self.name}"


class CelebrityVideo(models.Model):
    star_name = models.CharField(max_length=100) # 'Shraddha Kapoor'
    quote = models.TextField(blank=True)
    video_file = models.FileField(upload_to="celebrities/videos/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to="celebrities/thumbs/", blank=True, null=True)
    aspect_ratio = models.CharField(max_length=20, default="9:16")
    duration_label = models.CharField(max_length=50, default="30 to 60s · vertical")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.star_name


class Transformation(models.Model):
    member_name = models.CharField(max_length=100, blank=True)
    before_image = models.ImageField(upload_to="transformations/before/", blank=True, null=True)
    after_image = models.ImageField(upload_to="transformations/after/", blank=True, null=True)
    before_image_url = models.TextField(blank=True, null=True) # Supports data URLs or external CDN
    after_image_url = models.TextField(blank=True, null=True)
    metric_label = models.CharField(max_length=120, default="-8.4 kg fat · +3.2 kg muscle")
    timeline_weeks = models.PositiveIntegerField(default=12)
    program_attended = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"Transformation - {self.member_name or self.metric_label}"


class Coach(models.Model):
    name = models.CharField(max_length=120)
    role_title = models.CharField(max_length=120) # 'Founder & Head Coach'
    celebrities_trained = models.CharField(max_length=255, blank=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to="coaches/", blank=True, null=True)
    photo_url = models.TextField(blank=True, null=True)
    specialties = models.JSONField(default=list, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.name} ({self.role_title})"


class MembershipTier(models.Model):
    tier_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price_display = models.CharField(max_length=80) # '₹18,000 / month'
    billing_period = models.CharField(max_length=50, default="Monthly")
    features_list = models.JSONField(default=list)
    is_highlighted = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.tier_name


class FAQItem(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    page_category = models.CharField(max_length=50, default='home')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question


class ShopProduct(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=50, default="Apparel")
    price = models.CharField(max_length=50, default="₹2,499")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="shop/", blank=True, null=True)
    is_available = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class UploadedMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('photo', 'Photo / Image'),
        ('video', 'Video'),
        ('document', 'Document'),
    ]
    title = models.CharField(max_length=150)
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPE_CHOICES, default='photo')
    file = models.FileField(upload_to="uploads/%Y/%m/")
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.title} ({self.media_type})"
