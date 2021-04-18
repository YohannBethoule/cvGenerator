# Generated by Django 3.0.3 on 2021-04-10 17:49

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cvGeneratorBO', '0005_auto_20210410_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='siteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteTitle', models.CharField(max_length=255)),
                ('primary_color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('secondary_color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('nav_background_color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('nav_items_color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('dataManager', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='siteSettings', to='cvGeneratorBO.DataManager')),
            ],
        ),
    ]
