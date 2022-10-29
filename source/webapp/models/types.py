from django.db import models
from webapp.models.base import BaseModel


class Types(BaseModel):
    type_name = models.CharField(
        max_length=100,
        null=False,
        verbose_name="Type")

    def __str__(self):
        return f"{self.type_name}"

    class Meta:
        db_table = "type"
        verbose_name = "Type"
        verbose_name_plural = "Types"
