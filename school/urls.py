from django.urls import path
from rest_framework.routers import DefaultRouter

from school.views import *

from school.apps import SchoolConfig

app_name = SchoolConfig.name

# Описание маршрутизации для ViewSet
router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'payments', PaymentsViewSet, basename='payments')
urlpatterns = router.urls

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_view'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('Payments/', PaymentsListAPIView.as_view(), name='payments_list'),
] + router.urls
