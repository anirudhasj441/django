from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.models import Session
def index(request):
    return render(request,"index.html")