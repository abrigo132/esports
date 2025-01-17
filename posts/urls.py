from django.urls import path

from .views import ListPostsView, DetailPostView

urlpatterns = [
    path("posts/<int:id>/", DetailPostView.as_view(), name="detail post"),
    path("posts/", ListPostsView.as_view(), name="list posts"),
]
