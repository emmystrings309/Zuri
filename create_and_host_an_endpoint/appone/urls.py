from django.urls import path
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('api/', views.my_endpoint, name='my_endpoint'),
]
