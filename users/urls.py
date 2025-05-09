# users/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import SignupView, signup_page, login_page

urlpatterns = [
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 로그인
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 토큰 갱신

    # 페이지
    path('signup/', signup_page, name='signup_page'),
    path('login/', login_page, name='login_page'),
]
