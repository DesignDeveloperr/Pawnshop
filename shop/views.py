from django.http import HttpRequest
from django.shortcuts import render, redirect

from shop.services import _add_product
from user.services import _user_is_auth


def sell_page(request: HttpRequest):
    if _user_is_auth(request):
        if request.method == 'GET':
            return render(request, 'sell.html', {'auth': _user_is_auth(request)})

        if request.method == 'POST':
            return _add_product(request)
    else:
        return redirect('login')


def products_page(request: HttpRequest):
    if _user_is_auth(request):
        if request.method == 'GET':
            return render(request, 'products.html', {'auth': _user_is_auth(request)})
