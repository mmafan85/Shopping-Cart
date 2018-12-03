from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('checkout/', views.welcome, name='checkout'),
    path('receipt/', views.welcome, name='receipt'),
]