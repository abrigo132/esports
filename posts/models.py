from django.db import models
from django.db.models import ForeignKey

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


class Comment(models.Model):
    """
    Модель для комментариев к определённому посту
    """

    user = ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=1000, null=False)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )  # Вложенные комментарии
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} in {self.post.id}"

    class Meta:
        ordering = ["-created_at"]
