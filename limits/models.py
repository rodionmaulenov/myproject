from django.db import models


class Limit(models.Model):
    entry = models.DateField(blank=True, null=True)
    exit = models.DateField(blank=True, null=True)
    date_update = models.DateField(blank=True, null=True)
    person = models.ForeignKey('persons.Person', on_delete=models.PROTECT)

