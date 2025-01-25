from django.db import models

# Create your models here.
class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=100)

    def __str__(self):
        return self.store_name