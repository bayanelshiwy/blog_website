from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_edit', kwargs={'pk': self.pk})