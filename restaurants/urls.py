from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, restaurant_detail_page

router = DefaultRouter()
router.register(r'', RestaurantViewSet, basename='restaurant')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:id>/detail/', restaurant_detail_page, name='restaurant_detail'),
]
