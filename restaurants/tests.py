from rest_framework.test import APITestCase
from django.urls import reverse
from restaurants.models import Restaurant


class RestaurantViewTestCase(APITestCase):
    def setUp(self):
        self.restaurant_data = {
            "name": "good Restaurant",
            "description": "Nice food",
            "address": "Seoul, Korea",
            "contact": "010-1234-5678",
            "open_time": "09:00:00",
            "close_time": "21:00:00",
            "last_order": "20:30:00",
            "regular_holiday": "TUE"
        }

        self.restaurant = Restaurant.objects.create(**self.restaurant_data)

    def test_restaurant_list_view(self):
        """전체 restaurant 목록을 가져오는 테스트"""
        url = reverse('restaurant-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], self.restaurant.name)

    def test_restaurant_post_view(self):
        """restaurant 생성 테스트"""
        url = reverse('restaurant-list')
        new_data = self.restaurant_data.copy()
        new_data['name'] = "New Restaurant"

        response = self.client.post(url, new_data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Restaurant.objects.count(), 2)
        self.assertEqual(Restaurant.objects.latest('id').name, "New Restaurant")

    def test_restaurant_detail_view(self):
        """단일 restaurant 조회 테스트"""
        url = reverse('restaurant-detail', kwargs={'pk': self.restaurant.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.restaurant.name)

    def test_restaurant_update_view(self):
        """restaurant 정보 수정 테스트"""
        url = reverse('restaurant-detail', kwargs={'pk': self.restaurant.id})
        updated_data = self.restaurant_data.copy()
        updated_data['name'] = "Updated Restaurant"

        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "Updated Restaurant")

    def test_restaurant_delete_view(self):
        """restaurant 삭제 테스트"""
        url = reverse('restaurant-detail', kwargs={'pk': self.restaurant.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Restaurant.objects.count(), 0)
