from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_list, name='app_list'),
    path('app/<int:pk>/', views.app_detail, name='app_detail'),
    path('app/new/', views.app_new, name='app_new'),
]