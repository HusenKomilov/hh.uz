from rest_framework import generics
from vacancy import models, serializers


class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.CategoryFilterSerializer
    filterset_fields = ('category',)
