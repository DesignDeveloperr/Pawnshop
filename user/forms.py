from django import forms


class RegisterUserForm(forms.Form):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(max_length=255)
    password_reply = forms.CharField(max_length=255)


class LoginUserForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    fill_in = forms.BooleanField(widget=forms.CheckboxInput, required=False)
