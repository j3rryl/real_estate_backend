from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from django.db.models import Q
from .models import Property
from .serializers import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    renderer_classes = [JSONRenderer]
    def get_queryset(self):
        """
        Override the default queryset to include filtering based on query parameters.
        """
        queryset = super().get_queryset()
        query = self.request.query_params.get('q', None)  # Get the 'q' parameter from the request

        if query:
            queryset = queryset.filter(
                Q(location__icontains=query) |
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        return queryset
