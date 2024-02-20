from rest_framework import serializers
from vacancy import models


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ('pk', 'title')


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = ('pk', 'title', 'region')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('title', 'parent', 'slug')


class MasterSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.MasterType
        fields = ('title', 'category')


class CategoryFilterSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    region = RegionSerializer()
    district = DistrictSerializer()

    class Meta:
        model = models.Vacancy
        fields = ('pk', 'category', 'from_price', 'to_price', 'region', 'district')


class VacancySerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    district = DistrictSerializer()

    class Meta:
        model = models.Vacancy
        fields = (
            'id', 'title', 'from_price', 'to_price', 'company', 'master', 'category', 'parent',)
