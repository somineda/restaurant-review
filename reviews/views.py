from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from restaurants.models import Restaurant

# 리뷰 리스트 및 생성 (식당 ID 기준)
class ReviewListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, restaurant_id):
        reviews = Review.objects.filter(restaurant_id=restaurant_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, restaurant_id):
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, restaurant=restaurant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 리뷰 상세 조회/수정/삭제
class ReviewDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, review_id, restaurant_id=None):
        if restaurant_id:
            return get_object_or_404(Review, id=review_id, restaurant_id=restaurant_id)
        return get_object_or_404(Review, id=review_id)

    def get(self, request, review_id, restaurant_id=None):
        review = self.get_object(review_id, restaurant_id)
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)

    def put(self, request, review_id, restaurant_id=None):
        review = self.get_object(review_id, restaurant_id)
        if request.user != review.user:
            return Response({'error': '권한 없음'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ReviewDetailSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id, restaurant_id=None):
        review = self.get_object(review_id, restaurant_id)
        if request.user != review.user:
            return Response({'error': '권한 없음'}, status=status.HTTP_403_FORBIDDEN)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def review_list_page(request):
    return render(request, 'review_list.html')

def review_create_page(request):
    return render(request, 'review_create.html')

def review_create(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == "POST":
        Review.objects.create(
            restaurant=restaurant,
            user=request.user,
            comment=request.POST["comment"]
        )
        return redirect("/")
    return render(request, "review_create.html", {"restaurant": restaurant})
