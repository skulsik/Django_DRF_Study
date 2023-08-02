from rest_framework import serializers

from school.models import *


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'id',
            'name',
            'preview',
            'description',
            'url',
            'owner',
            'is_active'
        ]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_count(self, object):
        return Lesson.objects.all().count()

    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'preview',
            'description',
            'owner',
            'is_active',
            'lesson_count',
            'lessons'
        ]


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = [
            'user',
            'date_pay',
            'name_of_payment',
            'payment_amount',
            'payment_method',
            'is_active'
        ]
