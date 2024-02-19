from django.urls import path, include
from django.contrib import admin
from main import views
from single_pages import views 

app_name = "single_pages"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("restaurants_detail/<int:restaurant_id>/", views.detail, name="detail"),
    path("review_add/<int:restaurant_id>", views.review_add, name="review_add")
]