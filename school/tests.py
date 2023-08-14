from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from school.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='user@test.com',
            password='0000'
        )
        self.client.force_authenticate(user=self.user)
        self.lesson = Lesson.objects.create(
            name='test',
            description='test',
            url='https://www.youtube.com'
        )

    def test_view_list_lesson(self):
        """ Тест получение списка уроков """
        response = self.client.get(
            '/lesson/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        """ Тест создания урока """
        data = {
            'name': 'test',
            'description': 'test',
            'url': 'https://www.youtube.com',
            'owner': 1
        }
        response = self.client.post(
            reverse('school:lesson_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_view_lesson(self):
        """ Тест получение урока """
        response = self.client.get(
            '/lesson/5/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 5, 'name': 'test', 'preview': None, 'description': 'test', 'url': 'https://www.youtube.com', 'owner': None, 'is_active': True}
        )

    def test_delete_lesson(self):
        """ Тест удаления урока """
        Lesson.objects.create(
            name='test',
            description='test',
            url='https://www.youtube.com'
        )
        response = self.client.delete(
            '/lesson/delete/4/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='user@test.com', password='0000')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='test',
            description='test'
        )

    def test_create_subscription(self):
        """ Тест создания подписки """
        user_list = User.objects.all()
        print(f'user id: {user_list[0].id}')
        course_list = Course.objects.all()
        print(f'user id: {course_list[0].id}')
        data = {
            'user': 5,
            'course': 1
        }
        response = self.client.post(
            reverse('school:subscription_create'),
            data=data
        )
        course_list = Course.objects.all()
        print(f'user id: {course_list}')
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
