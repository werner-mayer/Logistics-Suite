from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime 


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    client = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    date = models.DateField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client + ' ' + str(self.date)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


