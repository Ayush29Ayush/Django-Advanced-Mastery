from django.core.management.base import BaseCommand
from home.models import Store
from faker import Faker


class Command(BaseCommand):
    help = "Seeds fake data into the Store model"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Number of stores to create
        number_of_stores = 25

        for _ in range(number_of_stores):
            store_name = fake.company()
            store_address = fake.address()

            # Create and save the store instance
            store = Store(store_name=store_name, store_address=store_address)
            store.save()

        self.stdout.write(
            self.style.SUCCESS(f"Successfully seeded {number_of_stores} stores")
        )
