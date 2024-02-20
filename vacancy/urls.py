from django.urls import path
from vacancy import views

urlpatterns = [
    path('', views.CategoryListAPIView.as_view()),
]
