from django.urls import path

from . import views

urlpatterns = [
    path('', views.StartPageView.as_view(), name='startpage'),

    path('userprofile/<int:pk>', views.UserProfileView.as_view(), name='userprofile'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.user_change_password, name='change_password'),
    path('edit_userprofile/', views.edit_profile, name='edit_profile'),
    path('delete_picture/<int:pk>', views.user_delete_photo, name='delete_picture'),

    path('upload_picture/', views.user_upload_picture, name='upload_picture'),

    path('contests/', views.AllContestView.as_view(), name='all_contests'),
    path('contest/<int:pk>', views.contest_detail, name='contest_detail'),
    path('vote_in_contest/<int:contest_id>/<int:pic_id>', views.vote_in_contest, name='vote_in_contest'),
    path('send_to_contest/<int:contest_id>/<int:pic_id>', views.send_picture_to_contest, name='send_to_contest'),

]
