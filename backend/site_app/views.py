from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from .forms import LoginForm, PasswordForm, UserChangeDataForm, UserChangeExtraDataForm, UserRegistrationForm, \
    UserUploadImageForm
from .models import Contest, PictureContestRating, UserExtraData, UserImages, Votes

""" STATIC PAGES """


class StartPageView(TemplateView):
    template_name = "startpage.html"


class FrontPageView(TemplateView):
    template_name = 'elta/front_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_pics'] = UserImages.objects.all()[:40]
        return context


class AboutTeamMemberView(TemplateView):
    template_name = 'elta/about_team.html'


""" USERS """


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'elta/userprofile.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'rating']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['images'] = UserImages.objects.filter(user_id=self.kwargs.get('pk')).order_by('-date_uploaded')
        context['rating'] = UserExtraData.objects.get(user_id=self.kwargs.get('pk'))
        # to check if user on his/her profile
        context['current_user'] = self.kwargs.get('pk')
        return context


class ListUsers(ListView):
    model = User
    template_name = 'elta/all_users.html'


""" AUTH """


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object; UserExtraData, UserEventNotificationSettings tables would be created
            # automatically using post_save signal
            new_user.save()

            return render(request, 'elta/registration_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'elta/registration.html', {'user_form': user_form})


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
    return render(request, 'elta/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'elta/logout.html')


""" USER EDIT DATA """


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
        # changed
        if request.method == 'GET':
            return render(request, 'elta/change_userinfo.html', {'user_form': user_form,
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
        return render(request, 'elta/reset_password.html', {'form': form})
    else:
        return redirect('login')


""" MANAGING PICTURES """


class PictureView(TemplateView):
    template_name = 'elta/picture_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        picture = UserImages.objects.get(id=self.kwargs.get('pk'))
        context['picture'] = picture
        # to check if user is watching his/her picture
        context['picture_owner'] = picture.user
        # check if user has permission to delete pics from UserImages model
        context['can_delete_pictures'] = self.request.user.has_perm('site_app.delete_userimages')
        return context


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
                    if all_images_size + f.size <= 104857600:  # 100mb
                        instance = UserImages(user=request.user, picture=f)
                        instance.save()
                    else:
                        return HttpResponse('???? ???? ???????????? ?????????????????? ???????????? 500???? ???????????????????? ???? ????????????. '
                                            '?????????????? ?????????????????? ???????? ????????')
                return redirect('userprofile', request.user.pk)
        else:
            form = UserUploadImageForm()
        return render(request, 'elta/upload_picture.html', {'form': form})
    else:
        return redirect('login')


def user_delete_photo(request, pk):
    if request.user.is_authenticated:
        if request.method == 'GET':  # CHANGE TO POST
            user = request.user
            pic = UserImages.objects.get(id=pk)
            if pic.user == user or request.user.has_perm('site_app.delete_userimages'):
                pic.delete()
                return redirect('userprofile', request.user.pk)
            else:
                return HttpResponse('????????????, ???? ?????????????????? ?????????????? ?????????? ????????(???? ?????? ????????????) ?????? ?????????? ???????? ?????? ?? ????????.'
                                    ' ???? ???????? ???????????? ???? url-????, ?????????? ???????????????????? ???????????????? ?????? ??????????????????. '
                                    '?? ?????????? ????????????, ?????????????????? ?? ??????????????????????????????.')
    else:
        return redirect('login')


def send_picture_to_contest(request, contest_id, pic_id):
    if request.method == "GET":
        if request.user.is_authenticated:
            contest = Contest.objects.get(id=contest_id)

            if contest.active:
                # SOME SHIT IN QUERY-SETS, SURE IT CAN BE MUCH MORE BEAUTIFUL
                q = Contest.objects.filter(id=contest_id, pictures__id=pic_id)

                if len(q) == 0:  # if photo not in contest
                    # add it to contest
                    p = UserImages.objects.get(id=pic_id)
                    contest.pictures.add(p)
                else:
                    return HttpResponse('???? ?????? ?????????????? ?????? ???????? ???? ??????????????')
            else:
                return HttpResponse('?????????????? ??????????????????. ???? ???? ???????????? ???????????????????? ???????? ???? ???????????????????? ????????????????.')
            return redirect('contest_detail', contest_id)


""" CONTESTS """


class AllContestView(ListView):
    model = Contest
    template_name = 'elta/all_contests.html'


def contest_detail(request, pk):
    if request.method == 'GET':
        contest = get_object_or_404(Contest, pk=pk)

        # getting urls for all images in this contest and their pk
        images_for_contest_urls = []
        images_pk = []
        q = contest.pictures.all()
        for user_image in q:
            images_for_contest_urls.append(user_image.picture.url)
            images_pk.append(user_image.pk)
        # zip to iterate in template
        contest_pictures = zip(images_for_contest_urls, images_pk)

        if request.user.is_authenticated:
            user_pics = UserImages.objects.filter(user_id=request.user.pk).order_by('-date_uploaded')

            user_votes, created = Votes.objects.get_or_create(user__id=request.user.pk,
                                                              contest=contest,
                                                              defaults={'user': request.user,
                                                                        'contest': contest})

            return render(request, 'elta/contest_detail.html', {'object': contest,
                                                                'pictures': user_pics,
                                                                'contest_pictures': contest_pictures,
                                                                'votes_left': user_votes.votes_left})
        else:
            return render(request, 'elta/contest_detail.html', {'object': contest,
                                                                'contest_pictures': contest_pictures})


""" VOTE SYSTEM """


def vote_in_contest(request, contest_id, pic_id):
    if request.method == "GET":
        if request.user.is_authenticated:
            contest = Contest.objects.get(id=contest_id)

            # SHOULD BE DONE THROUGH TRANSACTIONS (probably)
            # check for database instance
            votes_q, created = Votes.objects.get_or_create(user=request.user,
                                                           contest_id=contest_id,
                                                           defaults={'votes_left': 3})
            pics_q, created = PictureContestRating.objects.get_or_create(picture_id=pic_id,
                                                                         contest_id=contest_id,
                                                                         defaults={'rating': 0})
            if contest.active:
                if votes_q.votes_left > 0:
                    # remove 1 vote
                    votes_q.votes_left -= 1
                    votes_q.save()
                    # add +1 to pic rating
                    pics_q.rating += 1
                    pics_q.save()
                else:
                    return HttpResponse('?????? ????????, ???? ???? ?????? ???????????????????????? ?????? ???????? 3 ????????????.')
            else:
                return HttpResponse('?????????????? ?? ??????????????????. ???? ???? ???????????? ????????????????????.')
            return redirect('contest_detail', contest_id)
        else:
            return redirect('login')


def vote_for_picture(request, pic_id):
    if request.method == 'GET':
        if request.user.is_authenticated:
            # gets owner of particular image and increases his/her rating
            # mb should be rewritten
            user = UserExtraData.objects.get(user_id=User.objects.get(userimages__id=pic_id).pk)
            user.rating += 1
            user.save()
            return redirect('frontpage')
        else:
            return redirect('login')
