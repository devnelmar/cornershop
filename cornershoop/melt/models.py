# Create your models here.
from django.db import models

from cornershoop.utils.models import BaseModel
from cornershoop.utils.choices import DAYS_OF_THE_WEEK


class Mealt(BaseModel):
    name = models.CharField(null=True, blank=True)
    date = models.CharField(
        verbose_name="estado de reporte",
        max_length=15,
        default=DAYS_OF_THE_WEEK[0][0],
        choices=DAYS_OF_THE_WEEK,
    )
    codigo = models.ForeignKey(CatalogueProductMga, on_delete=models.PROTECT)
