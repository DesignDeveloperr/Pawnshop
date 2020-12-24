import hashlib

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect

from user.forms import RegisterUserForm, LoginUserForm
from user.models import Users


def _get_user_from_session(request: HttpRequest) -> Users:
    """Get user object from email in session"""
    return Users.objects.get(email=request.session.get('email', None))


def _user_is_auth(request: HttpRequest) -> bool:
    """Checking for the relevance of data in the session"""
    try:
        if request.session.get('email', False):
            if _get_user_from_session(request).password == request.session['password']:
                return True
        else:
            return False
    except ObjectDoesNotExist:
        return False


def _encrypt_password(password: str) -> str:
    """Encrypts a password from a string"""
    salt = hashlib.md5(settings.SECRET_KEY.encode('utf-8')).hexdigest()
    return hashlib.sha256(str(salt + password).encode('utf-8')).hexdigest()


def register(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        if not _user_is_auth(request):
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                if not Users.objects.filter(email=form.cleaned_data['email']).exists():
                    if form.cleaned_data['password'] == form.cleaned_data['password_reply']:
                        Users.objects.create(
                            name=form.cleaned_data['name'],
                            surname=form.cleaned_data['surname'],
                            email=form.cleaned_data['email'],
                            password=_encrypt_password(form.cleaned_data['password'])
                        )

                        request.session['email'] = form.cleaned_data['email']
                        request.session['password'] = _encrypt_password(form.cleaned_data['password'])
                        request.session.set_expiry(24 * 60 * 60)

                        return JsonResponse({'code': 'success'})
                    else:
                        return JsonResponse({'code': 'error', 'msg': 'Пароли не совпадают'})
                else:
                    return JsonResponse({'code': 'error', 'msg': 'Аккаунт с такой почтой уже зарегистрирован'})
            else:
                return JsonResponse({'code': 'error', 'msg': 'Поля заполнены неверно'})


def login(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        if not _user_is_auth(request):
            form = LoginUserForm(request.POST)
            if form.is_valid():
                try:
                    if Users.objects.get(email=form.cleaned_data['email']).password == _encrypt_password(form.cleaned_data['password']):
                        request.session['email'] = form.cleaned_data['email']
                        request.session['password'] = _encrypt_password(form.cleaned_data['password'])
                        if not form.cleaned_data['fill_in']:
                            request.session.set_expiry(24 * 60 * 60)
                        return JsonResponse({'code': 'success'})
                    else:
                        return JsonResponse({'code': 'error', 'msg': 'Неверный пароль'})
                except ObjectDoesNotExist:
                    return JsonResponse({'code': 'error', 'msg': 'Пользователь не найден'})
            else:
                return JsonResponse({'code': 'error', 'msg': 'Поля заполнены неверно'})


def logout(request: HttpRequest):
    request.session.flush()
    return redirect('login')
