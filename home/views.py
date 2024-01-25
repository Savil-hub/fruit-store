from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Define a view for rendering the 'home.html' template.
def home(request):
    return render(request, 'home.html')


