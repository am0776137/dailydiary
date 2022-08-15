from django.urls import path
from diary import views


urlpatterns = [
    path("", views.home, name="diary-home"),
]