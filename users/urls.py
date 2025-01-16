from django.urls import path

from .views import ProfileView, SignUpView

urlpatterns = [
    path("profile/<int:id>/", ProfileView.as_view(), name="profile"),
    path("register", SignUpView.as_view(), name="register"),

]
