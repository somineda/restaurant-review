from django.contrib import admin
from django.urls import path, include
from config import views as page_views
from django.conf import settings
from django.conf.urls.static import static
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
    path('signup/', page_views.signup_page, name='signup'),
    path('login/', page_views.login_page, name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # 로그인
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 토큰 갱신
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
