from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.viewsets import ModelViewSet 

from advertisements.filters import AdvertisementFilter 
from advertisements.models import Advertisement 
from advertisements.serializers import AdvertisementSerializer 
from advertisements.permissions import IsOwnerOrAdmin




class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = AdvertisementFilter
    filterset_fields = ['created_at', 'updated_at', 'status','creator']
   
    

    def get_queryset(self):
        param = self.request.query_params.get('creator')
        if param:
            return Advertisement.objects.filter(creator=param)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
               
#         if self.action in ["update", "partial_update", "destroy"]:
#             return [IsOwnerOrAdmin()]
        return []
