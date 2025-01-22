from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from products.models import Product


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = "products"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    #! field.ObjectField allows to use fields from other models and fields.KeywordField allows to use string fields i.e entire word passed in the search query should be same with the keyword field i.e brand_name in this case.
    brand_name = fields.ObjectField(properties={"brand_name": fields.KeywordField()})

    class Django:
        model = Product
        fields = [
            "title",
            "description",
            "category",
            "price",
            "brand",
            "sku",
            "thumbnail",
        ]
