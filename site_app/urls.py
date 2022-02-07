from django.urls import path

from . import views

urlpatterns = [
    path('', views.StartPageView.as_view(), name='startpage'),
    path('about_team', views.AboutTeamMemberView.as_view(), name='about_team'),

    path('userprofile/<int:pk>', views.UserProfileView.as_view(), name='userprofile'),
    path('all_users/', views.ListUsers.as_view(), name='all_users'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.user_change_password, name='change_password'),
    path('edit_userprofile/', views.edit_profile, name='edit_profile'),

    path('delete_picture/<int:pk>', views.user_delete_photo, name='delete_picture'),
    path('upload_picture/', views.user_upload_picture, name='upload_picture'),
    path('picture_detail/<int:pk>', views.PictureView.as_view(), name='picture_detail'),

    path('contests/', views.AllContestView.as_view(), name='all_contests'),
    path('contest/<int:pk>', views.contest_detail, name='contest_detail'),
    path('vote_in_contest/<int:contest_id>/<int:pic_id>', views.vote_in_contest, name='vote_in_contest'),
    path('send_to_contest/<int:contest_id>/<int:pic_id>', views.send_picture_to_contest, name='send_to_contest'),
    path('vote_for_users_pic/<int:pic_id>', views.vote_for_picture, name='vote_for_pic')
]
