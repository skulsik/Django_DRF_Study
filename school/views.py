from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from school.paginators import LessonPaginator, CoursePaginator
from school.permissions import IsOwner, IsStaff, IsStaffCreate
from school.serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny

from services.payment import GetPaymentLink


class CourseViewSet(ModelViewSet):
    """ Класс курса """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CoursePaginator


class SubscriptionCreateAPIView(CreateAPIView):
    """ Создание подписки """
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        subscription = serializer.save()
        subscription.user = self.request.user
        subscription.save()


class SubscriptionDestroyAPIView(DestroyAPIView):
    """ Удаление подписки """
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class LessonCreateAPIView(CreateAPIView):
    """ Создание урока """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsStaffCreate]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    """ Список уроков """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(RetrieveAPIView):
    """ Вывод одного урока """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsStaff]


class LessonUpdateAPIView(UpdateAPIView):
    """ Обновление урока """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsStaff]


class LessonDestroyAPIView(DestroyAPIView):
    """ Удаление урока """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PaymentsViewSet(ModelViewSet):
    """ Класс платежа """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentsListAPIView(ListAPIView):
    """ Список платежей """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['date_pay', 'name_of_payment', 'payment_method']
    ordering_fields = ['date_pay']


class PaymentGetLink(APIView):
    """ Получение ссылки на платеж """
    def get(self, request, id, price):
        # Получает курс по id
        course = Course.objects.get(id=id)
        # Создает посредством StripeAPI продукт и цену, получает ссылку на оплату курса
        payment_link = GetPaymentLink(name=course.name, price=price)

        return Response({
            'payment_link': payment_link.get_link(), })
