
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todolist.views import TodoListViewset

router = DefaultRouter()
router.register('todo', TodoListViewset)

urlpatterns = [
    path('v1/', include(router.urls)),
]