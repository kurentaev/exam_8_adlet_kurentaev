from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.db import models
from django.utils import timezone
from webapp.models.base import BaseModel
from django.utils.deconstruct import deconstructible
from webapp.managers import TaskProjectManager


def validate_digits_letters(word):
    for char in word:
        if not char.isdigit() and not char.isalpha():
            raise ValidationError('Enter only letters or digits')


@deconstructible
class CustomLengthValidator(BaseValidator):
    def __init__(self, limit_value=50, message=''):
        message = 'You enter %(limit_value)s symbols %(show_value)s'
        super(CustomLengthValidator, self).__init__(limit_value=limit_value, message=message)

    def compare(self, value, max_value):
        return max_value < value

    def clean(self, value):
        return len(value)


class Tasks(BaseModel):
    summary = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Summary',
        validators=(CustomLengthValidator(30), validate_digits_letters)
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Description'
    )
    status = models.ForeignKey(
        to='webapp.Statuses',
        related_name='status',
        on_delete=models.PROTECT,
        verbose_name='Status'
    )
    type = models.ManyToManyField(
        to='webapp.Types',
        related_name='type',
        blank=False
    )
    project = models.ForeignKey(
        to='webapp.Projects',
        related_name='tasks',
        on_delete=models.CASCADE,
        verbose_name='Project',
        blank=True,
        null=True
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
    )

    objects = TaskProjectManager()

    def __str__(self):
        return f"{self.summary} - {self.status} - {self.type}"

    class Meta:
        db_table = "tasks"
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
