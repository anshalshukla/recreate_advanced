from django.urls import path
from . import views

urlpatterns = [
    path("wait/", views.wait, name="wait"),
]
