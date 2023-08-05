from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from school.paginators import LessonPaginator, CoursePaginator
from school.permissions import IsOwner, IsStaff, IsStaffCreate
from school.serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class CourseViewSet(ModelViewSet):
    """ Простой ViewSet-класс """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CoursePaginator


class SubscriptionCreateAPIView(CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        subscription = serializer.save()
        subscription.user = self.request.user
        subscription.save()


class SubscriptionDestroyAPIView(DestroyAPIView):
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]#IsAuthenticated, IsStaffCreate]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]#IsAuthenticated]
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]#IsAuthenticated, IsOwner | IsStaff]


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]#IsAuthenticated, IsOwner | IsStaff]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]#IsAuthenticated, IsOwner]


class PaymentsViewSet(ModelViewSet):
    """ Простой ViewSet-класс """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentsListAPIView(ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['date_pay', 'name_of_payment', 'payment_method']
    ordering_fields = ['date_pay']
