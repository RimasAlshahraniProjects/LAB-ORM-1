from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("create/", views.create_post_view, name="create_post_view"),
    path("details/<int:post_id>/", views.post_details_view, name="post_details_view"),
    path("update/<int:post_id>/", views.post_update_view, name="post_update_view"),
    path("delete/<int:post_id>/", views.post_delete_view, name="post_delete_view"),


]  