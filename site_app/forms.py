from django import forms
from django.contrib.auth.models import User


class PasswordForm(forms.Form):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


class UserRegistrationForm(forms.ModelForm, PasswordForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'last_name')
        labels = {
            'first_name': 'Имя',
            'email': 'Электронная почта',
            'last_name': 'Фамилия'
        }
        help_texts = {
            'username': None,
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
