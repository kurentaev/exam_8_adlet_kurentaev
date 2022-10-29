from django.db import models
from django.db.models import Avg
from webapp.managers import ProductProjectManager
from webapp.models import BaseModel
from webapp.models.categories import CategoryChoices


class Products(BaseModel):
    name = models.CharField(
        verbose_name="Name",
        max_length=100,
        null=False,
        blank=False
    )
    category = models.CharField(
        verbose_name='Category',
        choices=CategoryChoices.choices,
        max_length=100,
        default=CategoryChoices.OTHER
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images',
        verbose_name='Image'
    )
    is_deleted = models.BooleanField(
        verbose_name='Deleted',
        default=False,
        null=False
    )

    objects = ProductProjectManager()

    def avg_ratings(self):
        return self.products.aggregate(
            Avg('rate')
        )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
