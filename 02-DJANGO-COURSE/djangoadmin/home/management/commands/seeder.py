from django.core.management.base import BaseCommand
from home.models import Customer, Order
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with fake customer and order data'

    def add_arguments(self, parser):
        parser.add_argument('--num_customers', type=int, default=50, help='Number of customers to generate')
        parser.add_argument('--num_orders', type=int, default=200, help='Number of orders to generate')

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Retrieve the arguments
        num_customers = kwargs['num_customers']
        num_orders = kwargs['num_orders']

        # Clear existing data
        self.stdout.write(self.style.WARNING("Clearing existing data..."))
        Customer.objects.all().delete()
        Order.objects.all().delete()

        # Generate fake customers
        customers = []
        self.stdout.write(self.style.SUCCESS(f"Generating {num_customers} fake customers..."))
        for _ in range(num_customers):  # Generate num_customers customers
            customer = Customer(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
            )
            customer.save()
            customers.append(customer)

        # Generate fake orders
        statuses = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']
        self.stdout.write(self.style.SUCCESS(f"Generating {num_orders} fake orders..."))
        for _ in range(num_orders):  # Generate num_orders orders
            order = Order(
                customer=random.choice(customers),
                order_date=fake.date_this_year(),
                total_amount=round(random.uniform(50.0, 500.0), 2),
                status=random.choice(statuses)
            )
            order.save()

        self.stdout.write(self.style.SUCCESS(f"Database seeding completed with {num_customers} customers and {num_orders} orders!"))
