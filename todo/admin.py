from django.contrib import admin

from todo.models import Todo, Tags

admin.site.register(Todo)
admin.site.register(Tags)

