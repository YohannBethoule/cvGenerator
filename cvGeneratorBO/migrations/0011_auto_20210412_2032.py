# Generated by Django 3.0.3 on 2021-04-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvGeneratorBO', '0010_auto_20210412_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='primary_font',
            field=models.CharField(choices=[('Lato', 'Lato (sans serif)'), ('Oswald', 'Oswald (sans serif)'), ('Ubuntu', 'Ubuntu (sans serif)'), ('Roboto', 'Roboto (sans serif)'), ('Arial', 'Arial (sans serif)'), ('Verdana', 'Verdana (sans serif)'), ('Times New Roman', 'Times New Roman (serif)'), ('Georgia ', 'Georgia  (serif)'), ('Courier New', 'Courier New (monospace)'), ('Brush Script MT', 'Brush Script MT (cursive)')], default='Ubuntu', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='secondary_font',
            field=models.CharField(choices=[('Lato', 'Lato (sans serif)'), ('Oswald', 'Oswald (sans serif)'), ('Ubuntu', 'Ubuntu (sans serif)'), ('Roboto', 'Roboto (sans serif)'), ('Arial', 'Arial (sans serif)'), ('Verdana', 'Verdana (sans serif)'), ('Times New Roman', 'Times New Roman (serif)'), ('Georgia ', 'Georgia  (serif)'), ('Courier New', 'Courier New (monospace)'), ('Brush Script MT', 'Brush Script MT (cursive)')], default='Ubuntu', max_length=255),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='ternary_font',
            field=models.CharField(choices=[('Lato', 'Lato (sans serif)'), ('Oswald', 'Oswald (sans serif)'), ('Ubuntu', 'Ubuntu (sans serif)'), ('Roboto', 'Roboto (sans serif)'), ('Arial', 'Arial (sans serif)'), ('Verdana', 'Verdana (sans serif)'), ('Times New Roman', 'Times New Roman (serif)'), ('Georgia ', 'Georgia  (serif)'), ('Courier New', 'Courier New (monospace)'), ('Brush Script MT', 'Brush Script MT (cursive)')], default='Ubuntu', max_length=255),
        ),
    ]