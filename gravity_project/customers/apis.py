from rest_framework import viewsets, filters
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.permissions import IsAuthenticated





class CustomerViewSet(viewsets.ModelViewSet):
    """Viewset for customer"""

    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']