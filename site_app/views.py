from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, TemplateView

from .forms import UserRegistrationForm, LoginForm, PasswordForm

"""
Start page
"""


class StartPageView(TemplateView):
    template_name = "front_page.html"


"""
Profiles
"""


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'userprofile.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'rating']


"""
authorization, authentification and so on
"""


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
            return render(request, 'registration_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form})


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
                    return HttpResponse('Disabled account. Please connect admin of the site.')
            else:
                return HttpResponse("Can't sign you in. Please connect admin of the site.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'logout.html')


def user_change_password(request):
    if request.user.is_authenticated:
        pk = request.user.pk
        user = get_object_or_404(User, pk=pk)
        if request.method == 'POST':
            form = PasswordForm(request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['password2']
                print(new_password)
                user.set_password(new_password)
                user.save()
                return redirect('login')
            else:
                return HttpResponse('form is not valid')
        else:
            form = PasswordForm()
        return render(request, 'reset_password.html', {'form': form, 'pk': pk})
    else:
        return redirect('login')
