from django.urls import path

from .views import (
    ProfileView,
    SignUpView,
    SocialLoginView,
    ListUsersView,
    ChangePasswordView,
)

urlpatterns = [
    path("profile/<int:id>/", ProfileView.as_view(), name="profile"),
    path("register/", SignUpView.as_view(), name="register"),
    path("social/login/", SocialLoginView.as_view(), name="social_login"),
    path("users/list/", ListUsersView.as_view(), name="users list"),
    path("change-password/", ChangePasswordView.as_view(), name="change password"),
]
