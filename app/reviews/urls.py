from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.CreateReviewView.as_view(),
         name='create_review'),
    path('review/list/', views.ListReviewView.as_view(),
         name='list_review'),
    path('review/<uuid:pk>/delete/',
         views.DeleteReviewView.as_view(), name='delete_review'),
    path('review/<uuid:pk>/detail/',
         views.RetrieveReviewView.as_view(), name='review_detail'),
    path('review/<uuid:pk>/update/',
         views.UpdateReviewView.as_view(), name='update_review'),
]
