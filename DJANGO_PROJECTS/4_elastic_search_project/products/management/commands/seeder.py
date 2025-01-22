import requests
from django.core.management.base import BaseCommand
from products.models import Product, Brand
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seeds the database with product and brand data from the dummyjson API or Faker if no data'

    def handle(self, *args, **kwargs):
        # Initialize Faker instance for generating dummy data
        fake = Faker()

        # Try to fetch data from the DummyJSON API
        url = "https://dummyjson.com/products?limit=1000"
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR('Failed to fetch data from API'))
            self.stdout.write(self.style.SUCCESS('Seeding with Faker data instead'))

            # If API fails, use Faker to generate fake products and brands
            self.seed_with_faker(fake)
        else:
            data = response.json()
            self.seed_with_api_data(data)

    def seed_with_api_data(self, data):
        for product_data in data['products']:
            try:
                # Check if the product already exists based on sku to prevent duplicates
                if Product.objects.filter(sku=product_data['sku']).exists():
                    self.stdout.write(self.style.SUCCESS(f"Product {product_data['title']} already exists, skipping"))
                    continue
                
                # Ensure the value of brand is set to the same value as brand_name
                brand_value = product_data.get('brand')

                if not brand_value:
                    self.stdout.write(self.style.WARNING(f"Skipping product {product_data['title']} due to missing brand"))
                    continue  # Skip the product if brand is missing

                # Create and save a new Brand instance
                brand, created = Brand.objects.get_or_create(brand_name=brand_value)

                # Create and save a new Product instance from API data
                product = Product(
                    title=product_data['title'],
                    description=product_data['description'],
                    category=product_data['category'],
                    price=product_data['price'],
                    brand_name=brand,  # Set the foreign key reference to the created brand
                    brand=brand_value,  # Set brand field with the same value
                    sku=product_data['sku'],
                    thumbnail=product_data['thumbnail']
                )
                product.save()
                self.stdout.write(self.style.SUCCESS(f"Successfully added product: {product.title}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error adding product {product_data['title']}: {str(e)}"))

    def seed_with_faker(self, fake):
        # Create 50 fake products and brands using Faker
        for _ in range(50):  # Create 50 fake products
            try:
                brand_value = fake.company()  # Get a random company name for the brand

                # Create and save a new Brand instance
                brand, created = Brand.objects.get_or_create(brand_name=brand_value)

                product = Product.objects.create(
                    title=fake.sentence(nb_words=5),
                    description=fake.text(),
                    category=fake.word(),
                    price=fake.random_number(digits=2),
                    brand_name=brand,  # Set the foreign key reference to the created brand
                    brand=brand_value,  # Set brand field with the same value
                    sku=fake.uuid4(),
                    thumbnail=fake.image_url(),
                )

                product.save()
                self.stdout.write(self.style.SUCCESS(f"Successfully added product: {product.title}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error adding product {product.title}: {str(e)}"))
