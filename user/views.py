from django.http import HttpRequest
from django.shortcuts import render, redirect

from shop.models import Products
from user.services import login, _user_is_auth, register, _get_user_from_session


def login_page(request: HttpRequest):
    if not _user_is_auth(request):
        if request.method == 'GET':
            return render(request, 'login.html', {'auth': _user_is_auth(request)})

        if request.method == 'POST':
            return login(request)
    else:
        return redirect('profile')


def register_page(request: HttpRequest):
    if not _user_is_auth(request):
        if request.method == 'GET':
            return render(request, 'register.html', {'auth': _user_is_auth(request)})

        if request.method == 'POST':
            return register(request)
    else:
        return redirect('profile')


def profile_page(request: HttpRequest):
    if _user_is_auth(request):
        if request.method == 'GET':
            return render(request, 'profile.html', {
                'auth': _user_is_auth(request),
                'name': _get_user_from_session(request).name,
                'surname': _get_user_from_session(request).surname,
                'email': _get_user_from_session(request).email,
                'count': Products.objects.filter(user=_get_user_from_session(request)).count(),
                'date': _get_user_from_session(request).date
            })
