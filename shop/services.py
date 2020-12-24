from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect

from shop.forms import ReviewForm, SellForm
from shop.models import Reviews, Products, Cart
from user.services import _get_user_from_session, _user_is_auth


def _add_review(request: HttpRequest, pk: int):
    if _user_is_auth(request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            Reviews.objects.create(
                product=Products.objects.get(pk=pk),
                user=_get_user_from_session(request),
                text=form.cleaned_data['text']
            )
            return redirect()


def _add_product(request: HttpRequest) -> JsonResponse:
    if _user_is_auth(request):
        form = SellForm(request.POST)
        if form.is_valid():
            Products.objects.create(
                user=_get_user_from_session(request),
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                image=request.FILES['image']
            )
            return JsonResponse({'code': 'success', 'msg': 'Товар успешно выставлен на продажу'})
        else:
            return JsonResponse({'code': 'error', 'msg': 'Поля заполнены неверно'})
    else:
        return JsonResponse({'code': 'error', 'msg': 'Ошибка авторизации'})


def get_products(request: HttpRequest, sort: str, search: str) -> JsonResponse:
    if _user_is_auth(request):
        if search == 'all':
            objects = Products.objects.all()
        else:
            objects = Products.objects.filter(name__iregex=search)

        if sort == 'name':
            objects.order_by('name')
        if sort == 'price':
            objects.order_by('price')

        data = []
        for obj in objects:
            data += [{
                'name': obj.name,
                'description': obj.description,
                'price': obj.price,
                'image': obj.image.url,
                'user': obj.user.surname + ' ' + obj.user.name,
                'id': obj.pk,
                'added': Cart.objects.filter(user=_get_user_from_session(request), product=obj).exists()
            }]

        return JsonResponse(data, safe=False)


def get_cart(request: HttpRequest):
    if _user_is_auth(request):
        objects = Cart.objects.filter(user=_get_user_from_session(request))
        data = []
        for obj in objects:
            data += [{
                'name': obj.product.name,
                'price': obj.product.price,
                'id': obj.pk
            }]
        return JsonResponse(data, safe=False)


def add_to_cart(request: HttpRequest, pk: int):
    if _user_is_auth(request):
        Cart.objects.create(
            user=_get_user_from_session(request),
            product=Products.objects.get(pk=pk)
        )
        return JsonResponse({'code': 'success'})
    else:
        return JsonResponse({'code': 'error', 'msg': 'Ошибка авторизации'})


def remove_from_cart(request: HttpRequest, pk: int):
    if _user_is_auth(request):
        try:
            Cart.objects.get(pk=pk).delete()
            return JsonResponse({'code': 'success'})
        except ObjectDoesNotExist:
            return JsonResponse({'code': 'error', 'msg': 'Обьект не найден'})
    else:
        return JsonResponse({'code': 'error', 'msg': 'Ошибка авторизации'})
