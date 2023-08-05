from rest_framework import serializers

from school.models import *
from school.validators import UrlValidator


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
        validators = [UrlValidator(field='name'), UrlValidator(field='description'), UrlValidator(field='url')]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'id',
            'user',
            'course'
        ]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_count(self, object):
        return Lesson.objects.all().count()

    def get_subscription(self, object):
        user = self.context['request'].user
        subscription_list = Subscription.objects.filter(user=user)
        for subscription in subscription_list:
            if subscription.course == object:
                return True
        return False

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
            'lessons',
            'subscription'
        ]
        validators = [UrlValidator(field='name'), UrlValidator(field='description')]


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
