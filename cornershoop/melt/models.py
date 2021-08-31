# Create your models here.
from django.db import models

from cornershoop.utils.models import BaseModel
from cornershoop.utils.choices import DAYS_OF_THE_WEEK


class Melt(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(
        verbose_name="dia de la semana",
        max_length=15,
        default=DAYS_OF_THE_WEEK[0][0],
        choices=DAYS_OF_THE_WEEK,
    )


class MeltSelectionUser(BaseModel):
    username = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    melt = models.ForeignKey(Melt, on_delete=models.PROTECT)
