from django.urls import path
from .views import TodoList

urlpatterns = [
    path('todos/', TodoList.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoList.as_view(), name='todo-detail'),
]
