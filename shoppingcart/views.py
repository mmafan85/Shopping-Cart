import json
from django.shortcuts import render
from django.http import HttpResponse
from shoppingcart.models import Product
from django.core.serializers import serialize

# Create your views here.
def welcome(request):
	if 'shopping_cart_items' in request.session:
		cart_items = request.session['shopping_cart_items']
	else:
		cart_items = []

	cart_contents = Product.objects.filter(pk__in=cart_items)
    
	return render(request, 'welcome.html', {'products': Product.objects.all(), 'cart_contents': cart_contents})

def addtocart(request):
	product_id = request.GET['product_id']

	if 'shopping_cart_items' in request.session:
		cart_items = request.session['shopping_cart_items']
	else:
		cart_items = []

	cart_items.append(product_id)

	request.session['shopping_cart_items'] = cart_items

	request.session.modified = True

	cart_contents = Product.objects.filter(pk__in=cart_items)
	
	return render(request, 'welcome.html', {'products': Product.objects.all(), 'cart_contents': cart_contents})

def removefromcart(request):
	product_id = request.GET['product_id']

	cart_items = request.session['shopping_cart_items']

	for item in cart_items:
		if item == product_id:
			cart_items.remove(item)

	request.session['shopping_cart_items'] = cart_items

	request.session.modified = True

	cart_contents = Product.objects.filter(pk__in=cart_items)
	
	return render(request, 'welcome.html', {'products': Product.objects.all(), 'cart_contents': cart_contents})

def checkout(request):
	cart_items = request.session['shopping_cart_items']

	cart_contents = Product.objects.filter(pk__in=cart_items)

	cart_total = 0

	for item in cart_contents:
		cart_total += item.price
	
	return render(request, 'checkout.html', {'products': Product.objects.all(), 'cart_contents': cart_contents, 'cart_total': cart_total})

def receipt(request):
	cart_items = request.session['shopping_cart_items']

	cart_contents = Product.objects.filter(pk__in=cart_items)

	cart_total = 0

	for item in cart_contents:
		cart_total += item.price

	buyer = {'name': request.POST['name'], 'address': request.POST['address'], 'city': request.POST['city'], 'state': request.POST['state'], 'zip': request.POST['zip'], 'card_number': request.POST['card_number'], 'cvv': request.POST['cvv'], 'exp': request.POST['exp']}
	
	return render(request, 'receipt.html', {'buyer': buyer, 'cart_contents': cart_contents, 'cart_total': cart_total})