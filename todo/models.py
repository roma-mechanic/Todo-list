from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Todo(models.Model):
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, related_name="todos")

    class Meta:
        ordering = ["status", "-created_time"]
