from django.db import models
from django.urls import reverse
from crum import get_current_user


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True,
                                   default=None)
    picture = models.ImageField(default="default")


    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(Blog, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_edit', kwargs={'pk': self.pk})