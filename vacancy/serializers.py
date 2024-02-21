from rest_framework import serializers
from vacancy import models


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ('pk', 'title')


class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = models.District
        fields = ('pk', 'title', 'region')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('title', 'slug')


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MasterType
        fields = ('title',)


class CategoryFilterSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    master = MasterSerializer()

    class Meta:
        model = models.Vacancy
        fields = ('pk', 'category', 'master', 'from_price', 'to_price')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = ('company',)


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = ('pk', 'title', 'from_price', 'to_price', 'region', 'district')


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = (
            'id', 'title', 'from_price', 'to_price', 'company', 'master', 'category', 'parent',)


class VacancyListCategorySerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    master = MasterSerializer()

    class Meta:
        model = models.Vacancy
        fields = (
            'id', 'title', 'company', 'region', 'degree', 'from_price', 'to_price', 'master', 'district', 'edu',
            'bandlik', 'grafik', 'part_time', 'is_company', 'is_position', 'is_job')
