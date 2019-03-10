from rest_framework import serializers
from todolist.models import TodoList, Tags

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = (
            'name',
            'date_tagged',
        )

class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tags.objects.all(),
        slug_field='name'
    )
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
            'required_revision',
            'created_at',
            'updated_at',
        )