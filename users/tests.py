from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse

User = get_user_model()


# 🔹 유저 모델 자체를 테스트하는 코드
class UserModelTest(TestCase):
    def setUp(self):
        self.test_user = {
            'email': 'user@example.com',
            'nickname': 'regularuser',
            'password': 'userpass123',
        }

        self.test_admin = {
            'email': 'admin@example.com',
            'nickname': 'adminuser',
            'password': 'adminpass123',
        }

    def test_user_manager_create_user(self):
        """일반 유저가 정상적으로 생성되는지 확인"""
        user = User.objects.create_user(**self.test_user)

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, self.test_user['email'])
        self.assertEqual(user.nickname, self.test_user['nickname'])
        self.assertTrue(user.check_password(self.test_user['password']))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.profile_image.url, '/media/users/blank_profile_image.png')

    def test_user_manager_create_superuser(self):
        """관리자(superuser)가 정상적으로 생성되는지 확인"""
        admin = User.objects.create_superuser(**self.test_admin)

        self.assertEqual(User.objects.filter(is_superuser=True, is_staff=True).count(), 1)
        self.assertEqual(admin.email, self.test_admin['email'])
        self.assertEqual(admin.nickname, self.test_admin['nickname'])
        self.assertTrue(admin.check_password(self.test_admin['password']))
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_active)
        self.assertEqual(admin.profile_image.url, '/media/users/blank_profile_image.png')


# 🔹 API 동작을 테스트하는 코드
class UserAPIViewTestCase(APITestCase):
    def setUp(self):
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user_data = {
            "email": "testuser@example.com",
            "nickname": "tester",
            "password": "strongpassword123"
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_signup(self):
        response = self.client.post(self.signup_url, {
            "email": "newuser@example.com",
            "nickname": "newbie",
            "password": "newpass123"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 2)

    def test_user_login(self):
        response = self.client.post(self.login_url, {
            "email": self.user_data["email"],
            "password": self.user_data["password"]
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("로그인 성공", response.data["message"])

    def test_user_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            "email": self.user_data["email"],
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.data)

    def test_user_logout(self):
        self.client.login(email=self.user_data["email"], password=self.user_data["password"])
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("로그아웃 성공", response.data["message"])
