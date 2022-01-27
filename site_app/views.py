import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect,  render
from django.views.generic import DetailView, ListView, TemplateView

from .forms import LoginForm, PasswordForm, UserChangeDataForm, UserChangeExtraDataForm, UserRegistrationForm, \
    UserUploadImageForm
from .models import Contest, UserExtraData, UserImages

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['images'] = UserImages.objects.filter(user_id=self.kwargs.get('pk')).order_by('-date_time_uploaded')
        context['rating'] = UserExtraData.objects.get(user_id=self.kwargs.get('pk'))
        context['current_user'] = self.kwargs.get('pk')
        return context


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

            # adding relative table for user
            new_user_extra_data = UserExtraData(user_id=new_user.id, rating=0)
            new_user_extra_data.save()

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


# using 2 modelforms for User and UserExtraData models
def edit_profile(request):
    if request.user.is_authenticated:

        # getting instances
        user = get_object_or_404(User, pk=request.user.pk)
        user_extra_data = get_object_or_404(UserExtraData, user=user)

        # init forms
        user_form = UserChangeDataForm(request.POST, instance=user)
        extra_data_form = UserChangeExtraDataForm(request.POST, instance=user_extra_data)

        if request.method == 'POST':
            # validating
            if user_form.is_valid() and extra_data_form.is_valid():
                # saving changes
                user_form.save()
                extra_data_form.save()
                return redirect('userprofile', request.user.pk)
        else:
            return render(request, 'change_userinfo.html', {'user_form': user_form,
                                                            'extra_data_form': extra_data_form})
    else:
        return redirect('login')


def user_change_password(request):
    if request.user.is_authenticated:
        pk = request.user.pk
        user = get_object_or_404(User, pk=pk)
        if request.method == 'POST':
            form = PasswordForm(request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['password2']
                user.set_password(new_password)
                user.save()
                return redirect('login')
            else:
                return HttpResponse('form is not valid')
        else:
            form = PasswordForm()
        return render(request, 'reset_password.html', {'form': form})
    else:
        return redirect('login')


def user_upload_picture(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserUploadImageForm(request.POST, request.FILES)
            files = request.FILES.getlist('picture')

            # getting size of all images for this user
            q = UserImages.objects.filter(user=request.user)
            all_images_size = 0
            for el in q:
                all_images_size += el.picture.size

            if form.is_valid():
                for f in files:
                    # so user won't be able to upload more than 500(100 for now) mb of files
                    # should be done customizable later
                    if all_images_size + f.size <= 104857600:    # 100mb
                        instance = UserImages(user=request.user, picture=f)
                        instance.save()
                    else:
                        return HttpResponse('Вы не можете загружать больше 500мб фотографий на сервер. '
                                            'Удалите некоторые ваши фото')
                return redirect('userprofile', request.user.pk)
        else:
            form = UserUploadImageForm()
        return render(request, 'upload_picture.html', {'form': form})
    else:
        return redirect('login')


class AllContestView(ListView):
    model = Contest
    template_name = 'all_contests.html'


class ContestDetailView(DetailView):
    model = Contest
    template_name = 'contest_detail.html'


def user_delete_photo(request, pk):
    if request.user.is_authenticated:
        if request.method == 'GET':    # CHANGE TO POST
            user = request.user
            try:
                picture = UserImages.objects.get(user=user, id=pk)
                if picture:
                    os.remove(picture.picture.path)
                    picture.delete()
                    return redirect('userprofile', request.user.pk)
                else:
                    return HttpResponse('Картинка не найдена. Свяжитесь с администратором.')
            except UserImages.DoesNotExist:
                return HttpResponse('Похоже, вы пытаетесь удалить чужое фото(фу так делать).'
                                    ' Не надо ходить по url-ам, админ специально кнопочки вам прикрутил. '
                                    'В любом случае, свяжитесь с администратором.')
    else:
        return redirect('login')
