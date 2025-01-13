from django.urls import path

from .views import ProfileView

urlpatterns = [
    path("user/<id:int>/", ProfileView.as_view(), name="profile"),
]
