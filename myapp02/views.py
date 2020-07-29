from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ("<h1>Welcome to views on app</h1>")

def home(request):
    return render (request,"myapp02/home.html",{'name':"Souvik"})


def child(request):
    return render (request,"child.html")

def sam(request):
    return render(request,"myapp02/sam.html")