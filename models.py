from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class NewPost(models.Model):
    post = models.TextField(max_length=1000)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
   
    def __str__(self):
        return f"Post by {self.posted_by.username} at {self.timestamp}"


class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(NewPost, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} liked {self.post.id}"