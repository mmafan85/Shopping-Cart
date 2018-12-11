from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('removefromcart/', views.removefromcart, name='removefromcart'),
    path('checkout/', views.checkout, name='checkout'),
    path('receipt/', views.receipt, name='receipt'),
]