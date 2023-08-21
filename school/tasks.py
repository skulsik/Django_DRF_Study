import time

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from users.models import User


@shared_task
def messaging_update_course(email, course):
    send_mail(
        subject=f'Обновление курса{course}',
        message=f'Посмотрите обновление курса!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False
    )


@shared_task
def checking_user_activity():
    # Читает список пользователей
    user_list = User.objects.all()

    for user in user_list:
        # Количество секунд в месяце
        time_month = 2592000

        # Получает дату текущую и дату последнего посещения пользователя в секундах
        time_now = time.time()
        time_user = time.mktime(user.last_login.timetuple())

        # Если пользователь не заходил больше месяца и не является superuser, ставит is_active = False
        if (time_now - time_user) > time_month:
            if user.is_superuser is not True:
                user.is_active = False
                user.save()
