from django.db import models

# Create your models here.


class Emails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=80)
    email = models.EmailField(max_length=255)
    title = models.TextField(max_length=255, blank=False)
    content = models.TextField(max_length=1000)
    replyContent = models.TextField(max_length=1000, blank=True)
    sendDate = models.TextField(max_length=20)
    sendForm = models.TextField(max_length=80)

    def __str__(self):
        return self.name
