from django.urls import path

from .views import ListPostsView, DetailPostView

urlpatterns = [
    path("<int:post_id>/", DetailPostView.as_view(), name="detail post"),
    path("", ListPostsView.as_view(), name="list posts"),
]
