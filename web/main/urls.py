from django.urls import path
from main import views

app_name = "main"
urlpatterns = [
    path("", views.main, name="main_page"),
    path("gu/<str:gu>/", views.restaurant_list, name="restaurant_list"),# gu_name이 str 타입으로 들어옴
    path("test/", views.test)
]
