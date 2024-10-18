from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_shop, name='register_shop'),
    path('list/', views.shop_list, name='shop_list'),
    path('search/', views.search_shops, name='search_shops'),
]
