from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurants.views import RestaurantViewSet
from .views import main_page, restaurant_detail_page


router = DefaultRouter()
router.register(r'', RestaurantViewSet, basename='restaurant')  # root path에서 처리

urlpatterns = [
    path('', include(router.urls)),
    path('', main_page, name='main-page'),
    path('detail/', restaurant_detail_page, name='restaurant-detail-page'),
]
