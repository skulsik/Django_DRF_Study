import stripe
from django.core.management import BaseCommand

from config import settings


class Command(BaseCommand):
    def __init__(self):
        self.name = "Лада седан"
        self.price = 2000000

    def handle(self, *args, **options):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Создает продукт, получает ответ в виде словаря
        product_dict: dict = stripe.Product.create(name=self.name)

        # Создает цену, получает ответ в виде словаря
        price_dict: dict = stripe.Price.create(
            unit_amount=self.price,
            currency="usd",
            recurring={"interval": "month"},
            product=product_dict.id,
        )

        # Создает ссылку, получает ответ в виде словаря
        link_dict: dict = stripe.PaymentLink.create(
            line_items=[
                {
                    "price": price_dict.id,
                    "quantity": 1,
                },
            ],
        )

        print(f"Ссылка на оплату товара: {link_dict.url}")
