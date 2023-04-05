from django.urls import path
from .views import BlogPostList, News

urlpatterns = [
    path('blog-posts/', BlogPostList.as_view(), name='blog-post-list'),
    
    path('blog-posts/<pbk>', News.as_view({
         'get':'get_post'
    }) ),
    
]
