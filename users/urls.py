from django.urls import path

from .views import ProfileView, SignUpView, SocialLoginView

urlpatterns = [
    path("profile/<int:id>/", ProfileView.as_view(), name="profile"),
    path("register/", SignUpView.as_view(), name="register"),
    path("social/login/", SocialLoginView.as_view(), name="social_login"),
]
