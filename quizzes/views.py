import random

from django.views.generic import DetailView, ListView

from quizzes.models import QuizStatement


class AllQuizzes(ListView):
    model = QuizStatement
    template_name = 'quizzes/all_quizzes.html'


class QuizView(DetailView):
    model = QuizStatement
    template_name = 'quizzes/quiz.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rendering_argument'] = random.randint(0, 1)
        context['num_of_questions'] = QuizStatement.objects.count()
        context['next_item_id'] = kwargs['object'].id+1
        return context
