import stripe
from config import settings


class GetPaymentLink:
    def __init__(self, name: str = "no name", price: int = 0):
        self.name = name
        self.price = price

    def get_link(self):
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

        return link_dict.url
