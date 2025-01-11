from django.template.defaultfilters import slugify
import uuid
from faker import Faker
from django.db import IntegrityError


fake = Faker()


def generateSlug(name, ModelClass):
    # Import inside the function to avoid circular import
    from myfirstapp.models import Brand

    new_slug = slugify(name)
    if ModelClass.objects.filter(slug=new_slug).exists():
        new_slug = f"{new_slug}-{str(uuid.uuid4()).split('-')[0]}"

    return new_slug


def bulk_create_brands(num_entries=10):
    from myfirstapp.models import (
        Brand,
    )  # Import inside function to avoid circular import

    brands_to_create = []
    for _ in range(num_entries):
        brand_name = fake.company()
        country = fake.country_code()  # Fake country code (e.g., 'IN', 'US', etc.)
        brands_to_create.append(Brand(brand_name=brand_name, country=country))

    try:
        Brand.objects.bulk_create(brands_to_create)
        return f"Bulk create operation successful for {num_entries} brands."
    except IntegrityError as e:
        return f"Integrity error during bulk create: {str(e)}"


def bulk_update_brands(num_entries=10):
    from myfirstapp.models import (
        Brand,
    )  # Import inside function to avoid circular import

    brands_to_update = []
    for _ in range(num_entries):
        brand = Brand.objects.order_by("?").first()  # Randomly select a brand
        if brand:
            new_brand_name = fake.company()
            brand.brand_name = new_brand_name
            brands_to_update.append(brand)

    if brands_to_update:
        Brand.objects.bulk_update(brands_to_update, ["brand_name"])
        return f"Bulk update operation successful for {len(brands_to_update)} brands."
    return "No brands were updated."


def bulk_delete_brands(num_entries=10):
    from myfirstapp.models import (
        Brand,
    )  # Import inside function to avoid circular import

    brands_to_delete = []
    for _ in range(num_entries):
        brand = Brand.objects.order_by("?").first()  # Randomly select a brand
        if brand:
            brands_to_delete.append(brand)

    if brands_to_delete:
        Brand.objects.filter(id__in=[brand.id for brand in brands_to_delete]).delete()
        return f"Bulk delete operation successful for {len(brands_to_delete)} brands."
    return "No brands were deleted."
