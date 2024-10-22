from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse 


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tag(models.Model):

    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag_name

class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


class Like (models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['post', 'user']

    def __str__(self):
        return f'{self.user} liked {self.post}'




