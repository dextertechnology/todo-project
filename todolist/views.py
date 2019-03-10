from rest_framework import viewsets

from todolist.models import TodoList, Tags
from todolist.serializers import TodoListSerializer, TagSerializer

class TodoListViewset(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class TagsViewset(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer