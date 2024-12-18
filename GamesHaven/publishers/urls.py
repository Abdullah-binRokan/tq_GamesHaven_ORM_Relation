from django.urls import path
from . import views

app_name = "publishers"

urlpatterns = [
    path("add/", views.add_publisher_view, name="add_publisher_view"),
    path("all/", views.all_publishers_view, name="all_publishers_view"),
    path("<publisher_id>/", views.detail_publisher_view, name="detail_publisher_veiw"),
]