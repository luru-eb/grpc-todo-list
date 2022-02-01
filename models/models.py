import datetime

from django.db import models
from django.utils import timezone


class Todo(models.Model):
    description = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    done_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.description}"

    def done(self):
        self.is_done = True
        self.done_at = timezone.now()
