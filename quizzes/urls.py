from django.urls import path

from . import views

urlpatterns = [
    path('all_quizes/', views.AllQuizzes.as_view(), name='all_quizzes'),
    path('quiz/<int:pk>', views.QuizView.as_view(), name='quiz'),
]
