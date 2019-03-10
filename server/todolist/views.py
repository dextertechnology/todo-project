from rest_framework import viewsets

from todolist.models import TodoList, Tags
from todolist.serializers import TodoListSerializer, TagSerializer

class TodoListViewset(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def get_queryset(self):
        queryset = TodoList.objects.all()
        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            queryset = TodoList.objects.filter(tags__slug=tag)
        return queryset



class TagsViewset(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer