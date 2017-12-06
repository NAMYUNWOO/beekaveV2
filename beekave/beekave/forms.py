from django.forms import EmailField

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core import validators

class UserCreationForm(UserCreationForm):
    email = EmailField(label=_("email"),error_messages={"invalid":"올바른 이메일주소를 입력해주세요"}, widget=forms.EmailInput(attrs={'class':'form-control',
    'placeholder': '이메일 주소'}),required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': '사용자 ID'}),required = True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': '비밀번호'}),required = True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': '비밀번호 재확인'}),required = True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)

        if r.count():
            raise  ValidationError("이미 존재하는 사용자 이름입니다.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("이미 존재하는 이메일 주소입니다.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("재확인 패스워드를 정확히 입력해주세요.")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
