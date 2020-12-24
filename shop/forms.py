from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField()


class SellForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField()
    price = forms.IntegerField()
