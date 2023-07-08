from django.urls import path

from todo.views import (
    index,
    TagsUpdateView,
    TagsDeleteView,
    TagsCreateView,
    TagsListView,
    TodoListView,
    TodoDeleteView,
    TodoUpdateView,
    TodoCreateView,
    todo_change_status,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tags-delete"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tags-update"),
    path("todo/", TodoListView.as_view(), name="todo-list"),
    path("todo/<int:pk>/delete/", TodoDeleteView.as_view(), name="todo-delete"),
    path("todo/<int:pk>/update/", TodoUpdateView.as_view(), name="todo-update"),
    path("todo/create/", TodoCreateView.as_view(), name="todo-create"),
    path("todo/<int:pk>/change_status", todo_change_status, name="todo-change_status"),
]

app_name = "todo"
