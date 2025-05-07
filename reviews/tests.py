from django.test import TestCase
from django.contrib.auth import get_user_model
from restaurants.models import Restaurant
from reviews.models import Review
from django.urls import reverse
from rest_framework.test import APITestCase

User = get_user_model()

class ReviewAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            nickname='tester',
            password='testpass123'
        )
        self.client.login(email='test@example.com', password='testpass123')

        self.restaurant = Restaurant.objects.create(
            name='Test Eatery',
            address='123 Test St',
            contact='123-456-7890',
        )

        self.review_data = {
            'restaurant': self.restaurant.id,
            'title': 'Great place!',
            'comment': 'I enjoyed the food and service.'
        }

        self.review = Review.objects.create(
            user=self.user,
            restaurant=self.restaurant,
            title='Old Title',
            comment='Old Comment'
        )

    def test_get_review_list(self):
        url = reverse('review-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_post_review(self):
        url = reverse('review-list')
        response = self.client.post(url, self.review_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Review.objects.count(), 2)

    def test_get_review_detail(self):
        url = reverse('review-detail', kwargs={'pk': self.review.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], self.review.title)

    def test_update_review(self):
        url = reverse('review-detail', kwargs={'pk': self.review.id})
        response = self.client.put(url, {
            'restaurant': self.restaurant.id,
            'title': 'Updated Title',
            'comment': 'Updated Comment'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_delete_review(self):
        url = reverse('review-detail', kwargs={'pk': self.review.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Review.objects.filter(pk=self.review.id).exists())

class ReviewModelTest(TestCase):
    def setUp(self):
        # 테스트용 유저 생성
        self.user = User.objects.create_user(
            email='reviewer@example.com',
            password='securepassword',
            nickname='reviewer123'
        )

        # 테스트용 식당 생성
        self.restaurant = Restaurant.objects.create(
            name='Review Place',
            description='A place to review',
            address='123 Review St',
            contact='010-5555-5555',
            open_time='10:00:00',
            close_time='21:00:00',
            last_order='20:30:00',
            regular_holiday='WED'
        )

        # 리뷰 데이터
        self.review_data = {
            'user': self.user,
            'restaurant': self.restaurant,
            'title': 'Amazing!',
            'comment': 'The food was delicious and the service was great.'
        }

    def test_create_review(self):
        """Review 모델이 정상적으로 생성되는지 테스트"""
        review = Review.objects.create(**self.review_data)

        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.restaurant, self.restaurant)
        self.assertEqual(review.title, self.review_data['title'])
        self.assertEqual(review.comment, self.review_data['comment'])
from django.test import TestCase

# Create your tests here.
