from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Blog
from .serializers import BlogPostSerializer, SinglePostSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status

class BlogPostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BlogPostList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class = BlogPostPagination


class News(viewsets.ViewSet):
    def get_post(self, request, pbk):
        post = Blog.objects.get(uuid=pbk)
        return Response(SinglePostSerializer(post).data,status=status.HTTP_200_OK)
