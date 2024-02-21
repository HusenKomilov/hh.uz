from rest_framework import generics, filters
from vacancy import models, serializers
from django_filters.rest_framework import DjangoFilterBackend


class DistrictListAPIView(generics.ListAPIView):
    queryset = models.District.objects.all().select_related('region')
    serializer_class = serializers.RegionSerializer
    filterset_fields = ('title',)


class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all().select_related('category', 'master', 'region', 'district')
    serializer_class = serializers.CategoryFilterSerializer
    filterset_fields = ('category', 'master')


class CompanyListAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all().select_related('category', 'master', 'region', 'district')
    serializer_class = serializers.CompanySerializer


class VacancyListAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all().order_by("?").select_related('category', 'master', 'region', 'district')
    serializer_class = serializers.VacancyListSerializer


class MasterListAPIView(generics.ListAPIView):
    queryset = models.MasterType.objects.all()
    serializer_class = serializers.MasterSerializer


class CategoryDetailListAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all().select_related('category', 'master', 'region', 'district')
    serializer_class = serializers.VacancyListCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = (
        'bandlik', 'grafik', 'part_time', 'region', 'district', 'degree', 'from_price', 'to_price', 'is_company',
        'is_position',
    )
    search_fields = ('title',)
