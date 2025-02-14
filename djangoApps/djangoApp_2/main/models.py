from django.db import models
from django.forms import DateTimeField


class UserAcc(models.Model):
    name = models.CharField(max_length=200, blank=False)
    surname = models.TextField(blank=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=200, blank=False)
    context = models.TextField()
    time = models.DateTimeField(auto_now=True)