from django.core.management import BaseCommand
from services.payment import GetPaymentLink


class Command(BaseCommand):
    def handle(self, *args, **options):
        link = GetPaymentLink(name="лада седан", price=500000)
        print(f"Ссылка на оплату товара: {link.get_link()}")
