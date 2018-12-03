from django.shortcuts import render
from django.http import HttpResponse
from shoppingcart.models import Product

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html', {'products': Product.objects.all()})