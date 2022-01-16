from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DetailView
from django.urls import reverse

from .forms import UserRegistrationForm, LoginForm, PasswordForm
from .serializers import UserSerializer
from rest_framework import generics

"""
Start page
"""


def startpage(request):
    return render(request, 'main/startpage.html')


"""
Api
"""


# снести
class UserApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


"""
Profiles
"""


# работает
class UserProfileView(LoginRequiredMixin, DetailView):
    # login_url = 'login'

    model = User
    template_name = 'main/userprofile.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'rating']


# падает
class ChangeUserInfoView(LoginRequiredMixin, UpdateView):
    # login_url = 'login'

    model = User
    template_name = 'main/change_userinfo.html'
    fields = ['username', 'first_name', 'email', 'is_active']
    username = None


"""
authorization, authentification and so on
"""


# раьотает, переделать рэдирект
def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'main/registration_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/registration.html', {'user_form': user_form})


# работает
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('userprofile', pk=request.user.pk)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


# работает
def user_logout(request):
    logout(request)
    return render(request, 'main/logout.html')


# работает
def user_change_password(request):
    if request.user.is_authenticated:
        pk = request.user.pk
        u = get_object_or_404(User, pk=pk)
        print(u.username)
        if request.method == 'POST':
            form = PasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password2']
                u.set_password(make_password(password))
                u.save()
        else:
            form = PasswordForm()
        return render(request, 'main/reset_password.html', {'form': form, 'pk': pk})
    else:
        return redirect('login')
