from django.urls import path
from .views import BlogPostList

urlpatterns = [
    path('blog-posts/', BlogPostList.as_view(), name='blog-post-list'),
]
