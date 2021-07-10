from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from rest_framework import generics, filters
from .forms import TaskForm
from . import serializers


class CreateView(generics.CreateAPIView):
    serializer_class = serializers.CartDetailSerializers


class ListView(generics.ListAPIView):
    serializer_class = serializers.CartListSerializers
    queryset = Region.objects.all()


class TaskDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.TaskDetailSerializers
    queryset = Task.objects.all()


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskListSerializers
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['Avilable_id']
    ordering = ['Avilable_id']


class TaskCreateView(generics.CreateAPIView):
    serializer_class = serializers.TaskListSerializers


class ChangeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CartChangedSerializers
    queryset = Region.objects.all()


# Create your views here.
def index(request):
    task = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'IAMFPR', 'task': task})


def about(request):
    return render(request, 'main/about.html')


def admin(request):
    return render(request, 'admin')


def post(request):
    return render(request, '23')


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
