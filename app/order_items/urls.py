from django.urls import path
from . import views

urlpatterns = [
    path('order-item/', views.CreateOrderItemView.as_view(),
         name='create_order_item'),
    path('order-item/list/', views.ListOrderItemView.as_view(),
         name='list_order_item'),
    path('order-item/<uuid:pk>/delete/',
         views.DeleteOrderItemView.as_view(), name='delete_order_item'),
    path('order-item/<uuid:pk>/detail/',
         views.RetrieveOrderItemView.as_view(), name='order_item_detail'),
    path('order-item/<uuid:pk>/update/',
         views.UpdateOrderItemView.as_view(), name='update_order_item'),
]
