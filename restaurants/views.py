from rest_framework.viewsets import ModelViewSet
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer
from django.shortcuts import render


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# 메인 페이지 (식당 목록)
def main_page(request):
    return render(request, 'main.html')

# 식당 상세 페이지 (리뷰 포함)
def restaurant_detail_page(request):
    return render(request, 'restaurant_detail.html')