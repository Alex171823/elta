from django.urls import path
from . import views

urlpatterns = [
    # startpage
    path('startpage/', views.startpage, name='startpage'),

    # api
    path('api/users/', views.UserApiView.as_view()),

    path('userprofile/<int:pk>', views.UserProfileView.as_view(), name='userprofile'),
    path('change_userprofile/', views.ChangeUserInfoView.as_view(), name='change_profile'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.user_change_password, name='change_password'),
]
