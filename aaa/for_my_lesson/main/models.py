from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True,upload_to='images')

    def __str__(self):
        return F"Title :: {self.title}"