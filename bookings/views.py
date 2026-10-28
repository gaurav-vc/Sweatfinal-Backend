from rest_framework import status, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import BookingLead
from .serializers import BookingLeadSerializer

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def submit_public_booking(request):
    """Public endpoint for 'Experience SWEAT', 'Fitness Assessment', and inquiries."""
    serializer = BookingLeadSerializer(data=request.data)
    if serializer.is_valid():
        lead = serializer.save()
        return Response({
            'success': True,
            'message': 'Your booking request has been received. Our team will confirm via WhatsApp shortly.',
            'lead_id': lead.id,
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CMSBookingLeadViewSet(viewsets.ModelViewSet):
    """CMS Studio viewset for viewing, filtering, and updating booking leads."""
    queryset = BookingLead.objects.all()
    serializer_class = BookingLeadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        lead_type = self.request.query_params.get('type')
        status_val = self.request.query_params.get('status')
        if lead_type:
            qs = qs.filter(lead_type=lead_type)
        if status_val:
            qs = qs.filter(status=status_val)
        return qs
