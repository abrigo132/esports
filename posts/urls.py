from django.urls import path

from .views import (
    ListPostsView,
    DetailPostView,
    ListPostsCommentsView,
    CommentListCreateView,
    CommentDetailView,
)

urlpatterns = [
    path("comments/", CommentListCreateView.as_view(), name="list comments"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="detail comment"),
    path(
        "<int:post_id>/comments/",
        ListPostsCommentsView.as_view(),
        name="list posts with comments",
    ),
    path("", ListPostsView.as_view(), name="list posts"),
    path("<int:pk>/", DetailPostView.as_view(), name="detail post")

]
