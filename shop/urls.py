from django.urls import path

from shop import views, services

urlpatterns = [
    path('sell/', views.sell_page, name='sell'),
    path('products/', views.products_page, name='products'),
    path('products/<str:search>/<str:sort>/', services.get_products),
    path('cart/', services.get_cart),
    path('cart/add/<int:pk>/', services.add_to_cart),
    path('cart/remove/<int:pk>/', services.remove_from_cart)
]
