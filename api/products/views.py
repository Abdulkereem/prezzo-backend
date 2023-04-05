from rest_framework import generics, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class ProductPagination(PageNumberPagination):
    page_size = 10 # or any other page size you want to use


class CategoryProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination 


    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)
        queryset = category.product_set.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page_number = request.query_params.get('page')
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
    

class CategoryList(viewsets.ViewSet):
    def get_all(self,request):
        category = Category.objects.all()
        return Response(CategorySerializer(category,many=True).data,status=status.HTTP_200_OK)
    


