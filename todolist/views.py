from rest_framework import viewsets

from todolist.models import TodoList
from todolist.serializers import TodoListSerializer

class TodoListViewset(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer