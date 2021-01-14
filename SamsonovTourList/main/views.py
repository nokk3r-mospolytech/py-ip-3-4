from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    task = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'IAMFPR', 'task': task})


def about(request):
    return render(request, 'main/about.html')


def admin(request):
    return render(request, 'admin')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = TaskForm()
    content = {
        'form': form
    }
    return render(request, 'main/create.html', content)

