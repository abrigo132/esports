from django.db import models

from users.models import User


class Post(models.Model):
    """
    Модель для постов
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    text = models.TextField(
        max_length=2000,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="likes_post", blank=True)
    dislikes = models.ManyToManyField(User, related_name="dislikes_post", blank=True)
    reposts = models.ManyToManyField(User, related_name="reposts_post", blank=True)

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"

    class Meta:
        ordering = ["-created_at"]
