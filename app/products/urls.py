from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.CreateProductView.as_view(), name='create_product'),
    path('product/list/', views.ListProductView.as_view(), name='list_product'),
    path('product/<uuid:pk>/delete/',
         views.DeleteProductView.as_view(), name='delete_product'),
    path('product/<uuid:pk>/detail/',
         views.RetrieveProductView.as_view(), name='product_detail'),
    path('product/<uuid:pk>/update/',
         views.UpdateProductView.as_view(), name='update_product'),
]
