from django.shortcuts import render

from todo.models import Todo


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
