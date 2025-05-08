from django.urls import path
from reviews.views import ReviewListCreateAPIView, ReviewDetailAPIView
from .views import review_list_page, review_create_page

urlpatterns = [
    path('restaurants/<int:restaurant_id>/reviews/', ReviewListCreateAPIView.as_view(), name='review-list'),
    path('reviews/<int:review_id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('list/', review_list_page, name='review-list-page'),
    path('create/', review_create_page, name='review-create-page'),
]
