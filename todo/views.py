from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Todo, Tags


def index(request):
    num_todos = Todo.objects.count()
    num_todos_done = Todo.objects.filter(status=True).count()
    num_toda_notdone = Todo.objects.filter(status=False).count()
    context = {
        "num_todos": num_todos,
        "num_todos_done": num_todos_done,
        "num_toda_notdone": num_toda_notdone
    }
    return render(request, "index.html", context=context)


class TagsListView(generic.ListView):
    model = Tags
    template_name = "tags/tags_list.html"


class TagsCreateView(generic.CreateView):
    model = Tags
    fields = "__all__"
    template_name = "tags/create_update.html"
    success_url = reverse_lazy("todo:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tags
    fields = "__all__"
    template_name = "tags/create_update.html"
    success_url = reverse_lazy("todo:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tags
    template_name = "tags/tags_confirm_delete.html"
    success_url = reverse_lazy("todo:tags-list")
