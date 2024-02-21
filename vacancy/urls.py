from django.urls import path
from vacancy import views

urlpatterns = [
    # home page
    path('', views.CategoryListAPIView.as_view()),
    path('vacancy/', views.VacancyListAPIView.as_view()),
    path('company/', views.CompanyListAPIView.as_view()),
    path('district/', views.DistrictListAPIView.as_view()),
    path('master/', views.MasterListAPIView.as_view()),

    # vacancy list
    path('vacancy-list/', views.CategoryDetailListAPIView.as_view()),
]
