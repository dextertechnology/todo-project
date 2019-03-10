
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todolist.views import TodoListViewset, TagsViewset

router = DefaultRouter()
router.register('todo', TodoListViewset)
router.register('tags', TagsViewset)

urlpatterns = [
    path('v1/', include(router.urls)),
]