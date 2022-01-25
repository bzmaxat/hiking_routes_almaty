from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

DEFAULT_USER_ID = 1


class Difficulty(models.Model):
    title = models.CharField("Difficulty", max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Difficulty"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='yes', blank=True, default='/yes/default.png')
    height = models.IntegerField()
    difficulty = models.ForeignKey(Difficulty, verbose_name="Difficulty", on_delete=models.SET_NULL, null=True)
    route = models.URLField(blank=True)
    completed = models.BooleanField(null=True, default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_list')
