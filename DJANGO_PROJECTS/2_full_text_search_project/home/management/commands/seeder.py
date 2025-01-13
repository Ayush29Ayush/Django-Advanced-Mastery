import requests
from django.core.management.base import BaseCommand
from home.models import Product

class Command(BaseCommand):
    help = 'Seeds the database with product data from the dummyjson API'

    def handle(self, *args, **kwargs):
        url = "https://dummyjson.com/products?limit=1000"
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR('Failed to fetch data from API'))
            return

        data = response.json()

        for product_data in data['products']:
            try:
                # Check if the product already exists based on sku to prevent duplicates
                if Product.objects.filter(sku=product_data['sku']).exists():
                    self.stdout.write(self.style.SUCCESS(f"Product {product_data['title']} already exists, skipping"))
                    continue
                
                # Create and save a new Product instance
                product = Product(
                    title=product_data['title'],
                    description=product_data['description'],
                    category=product_data['category'],
                    price=product_data['price'],
                    brand=product_data.get('brand'),
                    sku=product_data['sku'],
                    thumbnail=product_data['thumbnail']
                )
                product.save()
                self.stdout.write(self.style.SUCCESS(f"Successfully added product: {product.title}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error adding product {product_data['title']}: {str(e)}"))
