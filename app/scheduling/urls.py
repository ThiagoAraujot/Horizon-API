from django.urls import path
from . import views

urlpatterns = [
    path('scheduling/', views.CreateSchedulingView.as_view(),
         name='create_scheduling'),
    path('scheduling/list/', views.ListSchedulingView.as_view(),
         name='list_scheduling'),
    path('scheduling/<uuid:pk>/delete/',
         views.DeleteSchedulingView.as_view(), name='delete_scheduling'),
    path('scheduling/<uuid:pk>/detail/',
         views.RetrieveSchedulingView.as_view(), name='scheduling_detail'),
    path('scheduling/<uuid:pk>/update/',
         views.UpdateSchedulingView.as_view(), name='update_scheduling'),
]
