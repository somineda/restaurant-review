from django.urls import path
from .views import (
    ReviewListCreateAPIView,
    ReviewDetailAPIView,
    review_list_page,
    review_create_page,
    review_create
)

urlpatterns = [
    # REST API
    path('', ReviewListCreateAPIView.as_view(), name='review-list-create'),  # GET/POST: /restaurants/<id>/reviews/
    path('<int:review_id>/', ReviewDetailAPIView.as_view(), name='review-detail-by-restaurant'),  # GET/PUT/DELETE: /restaurants/<id>/reviews/<review_id>/

    # HTML 뷰 (선택적 웹 페이지용)
    path('list-page/', review_list_page, name='review-list-page'),
    path('create-page/', review_create_page, name='review-create-page'),
    path('create/', review_create, name='review-create'),
]
