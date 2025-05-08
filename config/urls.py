
from django.contrib import admin
from django.urls import path, include
from config import views as page_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('restaurants/', include('restaurants.urls')),
    path('reviews/', include('reviews.urls')),

    # HTML pages
    path('', page_views.main_page, name='main'),
    path('signup/', page_views.signup_page, name='signup'),
    path('login/', page_views.login_page, name='login'),
    path('restaurant-list/', page_views.restaurant_list_page, name='restaurant-list'),
    path('restaurant-detail/', page_views.restaurant_detail_page, name='restaurant-detail'),
    path('review-list/', page_views.review_list_page, name='review-list'),


]
