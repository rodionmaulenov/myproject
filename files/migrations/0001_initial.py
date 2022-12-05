# Generated by Django 4.1.3 on 2022-12-05 12:45

from django.db import migrations, models
import django.db.models.deletion
import files.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport', models.FileField(blank=True, null=True, upload_to=files.models.upload_to)),
                ('birth_certificate', models.FileField(blank=True, null=True, upload_to=files.models.upload_to)),
                ('children_birth_certificate', models.FileField(blank=True, null=True, upload_to=files.models.upload_to)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='persons.person')),
            ],
        ),
    ]