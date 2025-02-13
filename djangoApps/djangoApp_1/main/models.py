from django.db import models
class Users(models.Model):
    name = models.CharField(max_length=120, blank=False)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
