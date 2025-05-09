from django.shortcuts import render
from restaurants.models import Restaurant

def main_page(request):
    return render(request, 'main.html')

def signup_page(request):
    return render(request, 'signup.html')

def login_page(request):
    return render(request, 'login.html')

def restaurant_list_page(request):
    return render(request, 'restaurant_list.html')

def restaurant_detail_page(request):
    return render(request, 'restaurant_detail.html')

def review_list_page(request):
    return render(request, 'review_list.html')

def main_view(request):
    restaurants = Restaurant.objects.all()
    return render(request, "main.html", {"restaurants": restaurants})

