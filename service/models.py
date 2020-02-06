from django.db import models
from django.core.exceptions import ValidationError


def validate_positive(value):
    if value < 0:
        raise ValidationError(
            f'{value}s is not a positive number'
        )


class Deals(models.Model):
    customer = models.CharField(
        max_length=100
    )
    item = models.CharField(
        max_length=100
    )
    total = models.DecimalField(
        validators=[validate_positive],
        decimal_places=2,
        max_digits=20,
        verbose_name='Деньги'
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество'
    )
    date = models.DateTimeField()

    def __str__(self):
        return self.customer
