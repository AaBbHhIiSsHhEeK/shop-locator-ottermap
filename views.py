from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Shop
from .forms import ShopForm
from .utils import haversine

def register_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_list')
    else:
        form = ShopForm()
    return render(request, 'shops/register_shop.html', {'form': form})

def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shops/shop_list.html', {'shops': shops})

def search_shops(request):
    user_lat = float(request.GET.get('latitude'))
    user_lon = float(request.GET.get('longitude'))
    shops = Shop.objects.all()
    shop_distances = [(shop, haversine(user_lat, user_lon, shop.latitude, shop.longitude)) for shop in shops]
    shop_distances = sorted(shop_distances, key=lambda x: x[1])
    return render(request, 'shops/search_shops.html', {'shops': shop_distances})
