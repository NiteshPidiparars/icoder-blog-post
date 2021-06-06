from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # AdPI to post a comment
    path('postComment', views.postComment, name="postComment"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path('', views.blogHome, name="bloghome")
]
