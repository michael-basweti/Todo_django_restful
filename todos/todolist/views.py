from django.shortcuts import render
from rest_framework import viewsets
from .models import TodoList
from .serializers import TodoListSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all().order_by('-created_at')
    serializer_class = TodoListSerializer