from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blog_posts"
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
