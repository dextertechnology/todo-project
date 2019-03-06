from rest_framework import serializers
from todolist.models import TodoList

class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = (
            'title',
            'description',
            'tags',
            'is_done',
            'completed_at',
            'priority',
            'is_active',
            'required_revision'
        )