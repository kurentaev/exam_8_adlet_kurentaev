from django.db import models
from webapp.models.base import BaseModel


class Statuses(BaseModel):
    status_name = models.CharField(
        max_length=100,
        null=False,
        verbose_name="Status")

    def __str__(self):
        return f"{self.status_name}"

    class Meta:
        db_table = "status"
        verbose_name = "Status"
        verbose_name_plural = "Statuses"
