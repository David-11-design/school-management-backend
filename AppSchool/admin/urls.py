from django.urls import path, include
from rest_framework.routers import DefaultRouter
from AppSchool.admin import views

urlpatterns = [
    #path('students/', views.LoginView.as_view()),
    path('create-Teacher/', views.CreateTeacherView.as_view()),
    path('Create-Course/', views.CreateCourseView.as_view()),
    path('Create-Subject/', views.CreateSubjectView.as_view()),
    path('Get-Teachers/', views.GetTeacherView.as_view()),
    ]