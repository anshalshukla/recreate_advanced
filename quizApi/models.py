from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question = models.TextField()
    marks = models.IntegerField()
    negativeMarks = models.IntegerField()
    subject = models.TextField()

    def __str__(self):
        return self.question


class Options(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.TextField()

    def __str__(self):
        return self.choice


class AnswerKey(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, null=True)
    answer = models.OneToOneField(Options, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.answer


class ResponseSheet(models.Model):
    respondent = models.ForeignKey(User, on_delete=models.CASCADE)
    responseTo = models.OneToOneField(Question, on_delete=models.CASCADE, blank=True)
    responseIs = models.OneToOneField(Options, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.respondent
