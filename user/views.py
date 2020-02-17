from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def wait(request):
    return HttpResponse("To be created")
