from django.shortcuts import render
from .models import Task


# Create your views here.
def index(request):
    task = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'IAMFPR', 'task': task})


def about(request):
    return render(request, 'main/about.html')


def admin(request):
    return render(request, 'admin')

def create(request):
    return render(request, 'main/create.html')

