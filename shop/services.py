from django.http import HttpRequest
from django.shortcuts import redirect

from shop.forms import ReviewForm
from shop.models import Reviews, Products
from user.services import _get_user_from_session


def _add_review(request: HttpRequest, pk: int):
    form = ReviewForm(request.POST)
    if form.is_valid():
        Reviews.objects.create(
            product=Products.objects.get(pk=pk),
            user=_get_user_from_session(request),
            text=form.cleaned_data['text']
        )
        return redirect()