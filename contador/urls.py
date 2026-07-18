from django.urls import path
from . import views

urlpatterns = [
    path("", views.contador_view, name="contador"),
    path("http-async/", views.async_view, name="http_async"),
    path("http-sync/", views.sync_view, name="http_sync"),
]
