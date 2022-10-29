from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from webapp.managers import TaskProjectManager


class Projects(models.Model):
    start_date = models.DateField(
        verbose_name="Start date"
    )
    end_date = models.DateField(
        verbose_name="End date",
        blank=True,
        null=True
    )
    summary = models.CharField(
        verbose_name="Summary",
        max_length=100
    )
    description = models.TextField(
        verbose_name="Description"
    )
    is_deleted = models.BooleanField(
        verbose_name='Deleted',
        default=False,
        null=False
    )
    deleted_at = models.DateTimeField(
        verbose_name='Delete time',
        null=True,
        default=None
        #автозаполнение
    )
    user = models.ManyToManyField(
        to=User,
        related_name='Users',
        blank=True,
        verbose_name='User'
    )
    is_deleted_user = models.BooleanField(
        verbose_name='Deleted user',
        default=False,
        null=False
    )

    objects = TaskProjectManager()

    def __str__(self):
        return f"{self.summary}"

    class Meta:
        db_table = "project"
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
