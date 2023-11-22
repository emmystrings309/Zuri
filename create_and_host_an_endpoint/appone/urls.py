from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.my_endpoint, name='my_endpoint'),
]
