from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.CreateOrderView.as_view(), name='create_order'),
    path('order/list/', views.ListOrderView.as_view(), name='list_order'),
    path('order/<uuid:pk>/delete/',
         views.DeleteOrderView.as_view(), name='delete_order'),
    path('order/<uuid:pk>/detail/',
         views.RetrieveOrderView.as_view(), name='order_detail'),
    path('order/<uuid:pk>/update/',
         views.UpdateOrderView.as_view(), name='update_order'),
]
