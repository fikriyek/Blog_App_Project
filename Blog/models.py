from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Category Table
class CategoryTable(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None) 
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="Blog")
    category = models.ForeignKey(CategoryTable, on_delete=models.CASCADE, null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)

    STATUS_CHOICES = (
        ("d", "Draft"),
        ("p", "Published")
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='d')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    time_stamp = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment', null=True, blank=True)

    def __str__(self):
        return f"{self.content}"
    
class PostViews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post_views = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='post_views', null=True, blank=True)
    time_stamp = models.DateField(auto_now_add=True)

    
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes', null=True, blank=True)
    likes = models.BooleanField(default=False)