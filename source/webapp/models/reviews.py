from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from webapp.models import BaseModel
from webapp.managers import ProductProjectManager


class Reviews(BaseModel):
    author = models.ForeignKey(
        verbose_name='Author',
        to=User,
        related_name='reviews',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to='webapp.Products',
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Product',
        null=False,
        blank=False
    )
    review_text = models.TextField(
        verbose_name="Review",
        blank=False,
        null=False
    )
    rate = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Rate',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    is_deleted = models.BooleanField(
        verbose_name='Deleted',
        default=False,
        null=False
    )

    objects = ProductProjectManager()

    def __str__(self):
        return f"{self.author}"

    class Meta:
        db_table = "review"
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
