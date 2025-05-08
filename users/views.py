from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from users.serializers import SignupSerializer
from django.shortcuts import render

User = get_user_model()

#회원가입
def signup_page(request):
    return render(request, 'signup.html')

#로그인
def login_page(request):
    return render(request, 'login.html')

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 성공"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)
        return Response({"error": "이메일 또는 비밀번호가 올바르지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "로그아웃 성공"}, status=status.HTTP_200_OK)
