from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def index(request):
    return render(request, "bot/index.html")
