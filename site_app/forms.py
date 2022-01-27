from django import forms
from django.contrib.auth.models import User

from site_app.models import UserImages, UserExtraData


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


class UserUploadImageForm(forms.ModelForm):
    class Meta:
        model = UserImages
        exclude = ['user', 'date_time_uploaded']

        widgets = {
            'picture': forms.ClearableFileInput(attrs={'multiple': True, }),
        }


class UserChangeExtraDataForm(forms.ModelForm):
    class Meta:
        model = UserExtraData
        exclude = ['user', 'rating']


class UserChangeDataForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions', 'is_staff',
                   'is_active', 'is_superuser', 'last_login', 'date_joined']

        labels = {
            'first_name': 'Имя',
            'email': 'Электронная почта',
            'last_name': 'Фамилия'
        }
