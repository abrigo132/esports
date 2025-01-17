from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    reposts_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "text",
            "created_at",
            "updated_at",
            "image",
            "likes_count",
            "dislikes_count",
            "reposts_count",
        ]
        read_only_fields = [
            "user",
            "created_at",
            "updated_at",
            "likes_count",
            "dislikes_count",
            "reposts_count",
        ]

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_dislikes_count(self, obj):
        return obj.dislikes.count()

    def get_reposts_count(self, obj):
        return obj.reposts.count()
