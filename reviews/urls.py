from django.urls import path
from reviews.views import ReviewListCreateAPIView, ReviewDetailAPIView

urlpatterns = [
    path('restaurants/<int:restaurant_id>/reviews/', ReviewListCreateAPIView.as_view(), name='review-list'),
    path('reviews/<int:review_id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
