from django_filters import rest_framework as filters, DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter()
    updated_at = DateFromToRangeFilter()
    filter_backends = [DjangoFilterBackend]

    class Meta:
        model = Advertisement
        fields = ['created_at', 'updated_at', 'status']
