from django.contrib import admin
from django.urls import path, include
from config import views as page_views
from users.views import login_page, signup_page
from django.conf import settings
from django.conf.urls.static import static
from users.views import SignupView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('restaurants/', include('restaurants.urls')),
    path('reviews/', include('reviews.urls')),

    path('', page_views.main_page, name='main'),
    path('login/', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # 로그인
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 토큰 갱신
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
