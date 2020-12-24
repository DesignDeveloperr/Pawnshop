from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField()