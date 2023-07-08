from django.urls import path

from todo.views import (
    index,
    TagsUpdateView,
    TagsDeleteView,
    TagsCreateView,
    TagsListView
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tags-delete"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tags-update"),
]

app_name = "todo"
