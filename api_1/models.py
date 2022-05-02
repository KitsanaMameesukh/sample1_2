from django.db import models

# Create your models here.


class TodoLists(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255, blank=False)
    todo = models.TextField(max_length=500, blank=False)
    startDate = models.TextField(max_length=10)
    endDate = models.TextField(max_length=10)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
