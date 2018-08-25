from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    picture = models.ImageField(default="default.png")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_edit', kwargs={'pk': self.pk})




