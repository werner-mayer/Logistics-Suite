from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    client = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    date = models.DateTimeField()
    material = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client + ' ' + str(self.data)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})