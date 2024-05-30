from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    path('create', views.ProductCreateView.as_view(), name='product-create'),
    path('products', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', views.ProductRetreiveDestroyView.as_view(), name='product-detail-delete'),
    path('products/update/<int:pk>', views.ProductUpdateView.as_view(), name='product-update'),
]