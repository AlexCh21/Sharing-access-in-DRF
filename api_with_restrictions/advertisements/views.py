from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import request
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from .filters import AdvertisementFilter
from .models import Advertisement
from .permissions import IsOwnerOrViewOnly
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrViewOnly]
    filter_backends = [DjangoFilterBackend]
    filter_class = AdvertisementFilter

    filterset_fields = ['creator']

    def get_queryset(self):
        param = self.request.query_params.get('creator')
        if param:
            return Advertisement.objects.filter(creator=param)


