from django.urls import path
from . import views

urlpatterns = [
    path('create_tags', views.get_tags, name='post_list'),
]