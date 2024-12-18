from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('contact/', views.contact_view, name="contact_view"),
    path("mode/<mode>/", views.mode_view, name="mode_view"),
    path("test/params/<int:param1>/<param2>/", views.test_params_view, name="test_params_view")
]