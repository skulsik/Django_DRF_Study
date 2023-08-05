import re
from rest_framework.serializers import ValidationError


class UrlValidator:
    """ Проверка поля на введенные данные(ссылки запрещены, кроме youtube) """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile(r'https://')
        tmp_val = dict(value).get(self.field)
        result_search = re.findall(reg, tmp_val)
        if len(result_search) > 0:
            if 'https://www.youtube.com' not in tmp_val:
                raise ValidationError('Ссылки разрешены, только на youtube.com!')
            else:
                if len(result_search) != 1:
                    raise ValidationError('Ссылки разрешены, только на youtube.com!')
