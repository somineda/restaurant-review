from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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


