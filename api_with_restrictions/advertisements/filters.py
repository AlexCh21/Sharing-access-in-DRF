from django_filters import rest_framework as filters
from django_filters import FilterSet

from .models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter()
    update_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
