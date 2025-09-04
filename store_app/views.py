from django.shortcuts import render
from .form import Form

# Create your views here.
def baraa (request):
    form = Form()
    return render (request, 'baraa.html',{"form": form})