from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Lesson


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        pass

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
            'description': 'test'
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_view_lesson(self):
        """ Тест получение урока """
        Lesson.objects.create(
            name='test',
            description='test'
        )
        response = self.client.get(
            '/lesson/1/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'name': 'test', 'preview': None, 'description': 'test', 'url': None, 'owner': None, 'is_active': True}
        )

    def test_delete_lesson(self):
        """ Тест удаления урока """
        Lesson.objects.create(
            name='test',
            description='test'
        )
        print(Lesson.objects.all())
        response = self.client.post(
            '/lesson/delete/1/'
        )
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
