# Generated by Django 3.0.3 on 2021-04-12 18:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvGeneratorBO', '0011_auto_20210412_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
