from django import forms
from users.models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length = 3,
        widget=forms.TextInput(attrs = {"placeholder" : "사용자명 (3자리 이상)"}),
    )

    password = forms.CharField(
        min_length = 4,
        widget=forms.PasswordInput(attrs = {"placehodler" : "비밀번호 (4자리 이상)"}),
    )