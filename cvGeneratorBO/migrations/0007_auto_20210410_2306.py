# Generated by Django 3.0.3 on 2021-04-10 21:06

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvGeneratorBO', '0006_auto_20210410_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesettings',
            old_name='primary_color',
            new_name='primary_background_color',
        ),
        migrations.RenameField(
            model_name='sitesettings',
            old_name='secondary_color',
            new_name='primary_font_color',
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='secondary_background_color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='secondary_font_color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='ternary_color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
    ]
