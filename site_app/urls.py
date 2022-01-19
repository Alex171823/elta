from django.urls import path
from . import views
# from django.contrib.auth.views import login, logout

urlpatterns = [
    # startpage
    path('', views.StartPageView.as_view(), name='startpage'),

    path('userprofile/<int:pk>', views.UserProfileView.as_view(), name='userprofile'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.user_change_password, name='change_password'),
    path('userprofile/edit/', views.edit_profile, name='edit_profile'),

    path('upload_picture/', views.user_upload_picture, name='upload_picture'),
    # path('upload_picture/', views.UserUploadPictures.as_view(), name='upload_picture'),
]
