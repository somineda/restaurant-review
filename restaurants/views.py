from rest_framework.viewsets import ModelViewSet
from restaurants.serializers import RestaurantSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant
from reviews.models import Review


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# 메인 페이지 (식당 목록)
def main_page(request):
    return render(request, 'main.html')


def main_view(request):
    restaurants = Restaurant.objects.all()
    return render(request, "main.html", {"restaurants": restaurants})

def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    reviews = Review.objects.filter(restaurant=restaurant).select_related("user")

    if request.method == "POST":
        if request.user.is_authenticated:
            Review.objects.create(
                user=request.user,
                restaurant=restaurant,
                title=request.POST["title"],
                content=request.POST["content"]
            )
            return redirect("restaurant_detail", id=restaurant.id)
        else:
            return redirect("login")

    return render(request, "restaurant_detail.html", {
        "restaurant": restaurant,
        "reviews": reviews
    })

# 식당 상세 페이지 (리뷰 포함)
def restaurant_detail_page(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    reviews = Review.objects.filter(restaurant=restaurant)
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'reviews': reviews,
    })