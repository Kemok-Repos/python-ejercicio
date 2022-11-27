from django.db import models


class ScrappingData(models.Model):
    """Model to save scrapping data."""

    product_id = models.CharField(max_length=150, unique=True, blank=False, null=False)
    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    description = models.TextField(max_length=150, default='Dont have description')
    reviews = models.CharField(max_length=150)
    price = models.CharField(max_length=150)

    class Meta:
        db_table = "Products"

    def __str__(self):
        return self.name
