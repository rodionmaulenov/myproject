from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import timedelta
from django.db.models import F, Sum, Q
from limits.models import Limit


class Person(models.Model):
    class InProgram(models.TextChoices):
        NO_PROGRAM = 'NO', _('No program')
        SURROGACY = 'SUR', _('Surrogacy')
        EGG_DONOR = 'EGG', _('Egg donor')

    class BloodType(models.TextChoices):
        POSITIVE = 'POSITIVE', _('positive')
        NEGATIVE = 'NEGATIVE', _('negative')

    class Cesarean(models.TextChoices):
        NO_CESAREAN = 'NO', _('no cesarean')
        ONE_CESAREAN = 'ONE', _('one cesarean')
        TWO_CESAREAN = 'TWO', _('two cesarean')
        THREE_CESAREAN = 'THREE', _('three cesarean')
        MORE = 'MORE', _('more')

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    blood = models.PositiveSmallIntegerField(validators=[MaxValueValidator(limit_value=4)], default=0)
    blood_type = models.CharField(max_length=8, choices=BloodType.choices, default=BloodType.POSITIVE)
    cesarean = models.CharField(max_length=5, choices=Cesarean.choices, default=Cesarean.NO_CESAREAN)
    children = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(limit_value=5)])
    is_public = models.BooleanField(default=False)
    in_program = models.CharField(max_length=4, choices=InProgram.choices, default=InProgram.NO_PROGRAM)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return f'{self.name} - {self.country}'

    @property
    def get_days_in_ukr(self):
        queryset = Limit.objects.filter(person=self.pk).select_related('person').only('entry', 'exit', 'person')

        diff_180 = queryset.last().exit - timedelta(days=180)

        find_obj_between = queryset.filter(Q(entry__lte=diff_180) & Q(exit__gte=diff_180))

        if find_obj_between.exists():
            find_obj_days = find_obj_between[0].exit - diff_180
            objs_sum_days = queryset.filter(
                Q(entry__gt=find_obj_between[0].exit)
            ).aggregate(sum_date=Sum(F('exit') - F('entry')))
            diff_90_days = timedelta(days=90) - (objs_sum_days['sum_date'] + find_obj_days)
            return diff_90_days.days

        another_objs_sum_days = queryset.filter(
            Q(entry__gte=diff_180) & Q(exit__lte=queryset.last().exit)
        ).aggregate(sum_date=Sum(F('exit') - F('entry')))
        diff_90_days_1 = timedelta(days=90) - another_objs_sum_days['sum_date']
        return diff_90_days_1.days

    @property
    def get_days_when_date_update(self):
        queryset = Limit.objects.filter(person=self.pk).select_related('person').only('person')

        diff_180 = queryset.last().date_update - timedelta(days=180)

        find_obj_filter_queryset = queryset.filter(
            Q(entry__lte=diff_180) & Q(exit__gte=diff_180)
        )

        if find_obj_filter_queryset.exists():
            find_obj_days = find_obj_filter_queryset[0].exit - diff_180
            objs_sum_days = queryset.filter(
                Q(entry__gt=find_obj_filter_queryset[0].exit)
            ).aggregate(sum_date=Sum(F('exit') - F('entry')))
            diff_90_days = timedelta(days=90) - (objs_sum_days['sum_date'] + find_obj_days)
            return diff_90_days.days

        another_objs_sum_days = queryset.filter(
            Q(entry__gte=diff_180) & Q(exit__lte=queryset.last().exit)
        ).aggregate(sum_date=Sum(F('exit') - F('entry')))
        diff_90_days_1 = timedelta(days=90) - another_objs_sum_days['sum_date']
        return diff_90_days_1.days
