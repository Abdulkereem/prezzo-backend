from django.urls import path
from .views import CategoryProductList

urlpatterns = [
    path('category/<int:category_id>/products/', CategoryProductList.as_view(), name='category_products_api'),
    # other URL patterns...
]
