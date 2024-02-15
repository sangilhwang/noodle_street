from django import forms
from users.models import User
from django.core.exceptions import ValidationError

# 로그인 기능을 위한 form
class LoginForm(forms.Form):
    username = forms.CharField(
        min_length = 3,
        widget=forms.TextInput(attrs = {"placeholder" : "사용자명 (3자리 이상)"}),
    )

    password = forms.CharField(
        min_length = 4,
        widget=forms.PasswordInput(attrs = {"placehodler" : "비밀번호 (4자리 이상)"}),
    )

# 회원가입 기능을 위한 form
class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    birthday = forms.DateField()
    profile_image = forms.ImageField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data["username"]

        # username이 이미 사용중인지 검증
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"이미 사용중인 사용자명 {username} 입니다.")
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        
        # email이 이미 사용중인지 검증
        if User.objects.filter(email=email).exists():
            raise ValidationError(f"이미 사용중인 이메일주소입니다.")
        
        return email

    
    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        # 두 비밀번호가 서로 일치하는지 확인
        if password1 != password2:
            self.add_error("password2", "비밀번호가 서로 일치하지 않습니다.")

    # 전달받은 user 정보를 저장
    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        email = self.cleaned_data["email"]
        birthday = self.cleaned_data["birthday"]
        profile_image = self.cleaned_data["profile_image"]
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]

        user = User.objects.create_user(
            username = username,
            password = password1,
            email = email,
            birthday = birthday,
            profile_image = profile_image,
            first_name = first_name,
            last_name = last_name,
        )

        return user

    