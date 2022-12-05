from django.db import models

from persons.models import Person


def upload_to(instance, filename):
    return '{instance}/{filename}'.format(instance=instance.person.name, filename=filename)


class Document(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT)
    passport = models.FileField(upload_to=upload_to, blank=True, null=True)
    birth_certificate = models.FileField(upload_to=upload_to, blank=True, null=True)
    children_birth_certificate = models.FileField(upload_to=upload_to, blank=True, null=True)
