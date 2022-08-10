from .views import IndexPageView
from django.urls import path

app_name = "Djapp"

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
]
