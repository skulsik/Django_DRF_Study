from rest_framework import serializers

from school.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'name',
            'preview',
            'description',
            'is_active'
        ]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'name',
            'preview',
            'description',
            'url',
            'is_active'
        ]
