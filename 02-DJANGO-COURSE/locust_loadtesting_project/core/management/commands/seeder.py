from django.core.management.base import BaseCommand
from core.models import Product, Feedback
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seeds data into Product and Feedback models using Faker'

    def handle(self, *args, **kwargs):
        fake = Faker()

        num_products = 100  
        for _ in range(num_products):
            product = Product.objects.create(
                name=fake.company(),
                description=fake.text(),
                price=random.uniform(5.00, 100.00),  # Random price between 5.00 and 100.00
            )
            self.stdout.write(self.style.SUCCESS(f'Product created: {product.name}'))

        num_feedback = 50
        for _ in range(num_feedback):
            feedback = Feedback.objects.create(
                name=fake.name(),
                email=fake.email(),
                message=fake.text(),
            )
            self.stdout.write(self.style.SUCCESS(f'Feedback created: {feedback.name}'))
