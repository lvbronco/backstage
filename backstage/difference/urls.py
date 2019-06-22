from django.urls import path

from . import views

urlpatterns = [
    path(r'difference', views.difference, name='difference'),
    path(r'pythagorean', views.pythagorean, name='pythagorean'),
    path("", views.index, name="index")
]