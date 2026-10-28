from rest_framework import serializers
from .models import BookingLead

class BookingLeadSerializer(serializers.ModelSerializer):
    lead_type_display = serializers.CharField(source='get_lead_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    phone = serializers.CharField(source='whatsapp_number', required=False)
    preferred_day = serializers.CharField(source='selected_day', required=False, allow_blank=True)
    preferred_time = serializers.CharField(source='selected_time', required=False, allow_blank=True)
    admin_notes = serializers.CharField(source='notes', required=False, allow_blank=True)

    class Meta:
        model = BookingLead
        fields = [
            'id', 'lead_type', 'lead_type_display', 'full_name',
            'whatsapp_number', 'phone', 'selected_day', 'preferred_day',
            'selected_time', 'preferred_time', 'preferred_program',
            'status', 'status_display', 'notes', 'admin_notes',
            'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'whatsapp_number': {'required': False}
        }

    def validate(self, attrs):
        # Allow either phone or whatsapp_number
        if 'whatsapp_number' not in attrs and 'phone' not in self.initial_data:
            raise serializers.ValidationError({"phone": "Phone number is required."})
        return attrs
