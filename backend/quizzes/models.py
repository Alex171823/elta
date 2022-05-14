from django.db import models


class QuizStatement(models.Model):
    correct_statement = models.CharField(max_length=255, blank=False)
    wrong_statement = models.CharField(max_length=255, blank=False)
    explanation = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'

    def __str__(self):
        return f"{self.correct_statement} {self.wrong_statement} {self.explanation}"
