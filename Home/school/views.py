from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "Home/index.html")

def dashboard(request):
    return render(request, "students/student-dashboard.html")