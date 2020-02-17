from django.urls import path
from . import views

urlpatterns = [
    path("question/<int:pk>", views.QuestionBlock, name="question"),
    path("buildQuestion", views.BuildQuestion, name="buildQuestion"),
]
