from django.db import models

class BookingLead(models.Model):
    LEAD_TYPE_CHOICES = [
        ('experience', 'Experience SWEAT'),
        ('assessment', 'Fitness Assessment'),
        ('bootcamp', 'Bootcamp Inquiry'),
        ('pilates', 'Pilates Inquiry'),
        ('elite', 'Elite Membership'),
        ('general', 'General Contact'),
    ]
    STATUS_CHOICES = [
        ('new', 'New Lead'),
        ('whatsapp_sent', 'WhatsApp Contacted'),
        ('scheduled', 'Visit Scheduled'),
        ('completed', 'Visit Completed'),
        ('converted', 'Member Enrolled'),
        ('archived', 'Archived / Cold'),
    ]
    lead_type = models.CharField(max_length=40, choices=LEAD_TYPE_CHOICES, default='experience')
    full_name = models.CharField(max_length=150)
    whatsapp_number = models.CharField(max_length=30)
    selected_day = models.CharField(max_length=50, blank=True) # e.g. 'Today', 'Tomorrow', 'Sat'
    selected_time = models.CharField(max_length=50, blank=True) # e.g. '6:00 AM', '7:30 PM'
    preferred_program = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='new')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} ({self.get_lead_type_display()}) - {self.whatsapp_number}"
