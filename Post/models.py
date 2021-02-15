from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField(max_length=200, blank=False, null=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"

    