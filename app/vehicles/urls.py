from django.urls import path
from . import views

urlpatterns = [
    path('vehicle/', views.CreateVehicleView.as_view(), name='create_vehicle'),
    path('vehicle/list/', views.ListVehicleView.as_view(), name='list_vehicle'),
    path('vehicle/<uuid:pk>/delete/',
         views.DeleteVehicleView.as_view(), name='delete_vehicle'),
    path('vehicle/<uuid:pk>/detail/',
         views.RetrieveVehicleView.as_view(), name='vehicle_detail'),
    path('vehicle/<uuid:pk>/update/',
         views.UpdateVehicleView.as_view(), name='update_vehicle'),
]
