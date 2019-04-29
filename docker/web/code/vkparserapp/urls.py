from django.conf.urls import  url
from . import views
# from .models import Post
# from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', views.post_home, name='post_home'),


]
