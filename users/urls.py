from django.urls import path
from users.views import SignupView, LoginView, LogoutView, signup_page, login_page


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup_page, name='signup-page'),
    path('login/', login_page, name='login-page'),
]
