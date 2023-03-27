from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Blog
from .serializers import BlogPostSerializer

class BlogPostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BlogPostList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class = BlogPostPagination
