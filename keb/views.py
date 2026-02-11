from django.views import generic
from django.shortcuts import render
def Home(re):
    return render(re,"home.html")
