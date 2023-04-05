from django.urls import path
from .views import CategoryProductList, CategoryList

urlpatterns = [
    path('category/<int:category_id>/products/', CategoryProductList.as_view(), name='category_products_api'),
    path('categories/',CategoryList.as_view({
    'get':'get_all'
    }),name='category-list')
    # other URL patterns...
]
