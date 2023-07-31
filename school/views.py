from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from school.models import Course
from school.serializers import *


class CourseViewSet(ModelViewSet):
    """ Простой ViewSet-класс """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
