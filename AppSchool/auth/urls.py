from django.urls import path, include
from rest_framework.routers import DefaultRouter
from AppSchool.auth import views

urlpatterns = [
    path('aut/', views.AuthView.as_view())
]