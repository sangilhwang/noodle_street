from django.urls import path
from main import views

app_name = "main"
urlpatterns = [
    path("", views.main),
    path("test/", views.test),
    path("index/", views.index),
]