# Generated by Django 3.0.3 on 2021-04-09 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('jobTitle', models.TextField()),
                ('location', models.TextField()),
                ('mail', models.TextField()),
                ('phone', models.TextField()),
                ('github', models.TextField(null=True)),
                ('gitlab', models.TextField(null=True)),
                ('linkedin', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('client', models.TextField()),
                ('summary', models.TextField()),
                ('mission', models.TextField()),
                ('dataManager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cvGeneratorBO.DataManager')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=200)),
                ('published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('place', models.TextField()),
                ('date', models.TextField()),
                ('dataManager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cvGeneratorBO.DataManager')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cvGeneratorBO.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('title', models.TextField()),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cvGeneratorBO.Training')),
            ],
        ),
        migrations.CreateModel(
            name='Skillset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.TextField()),
                ('dataManager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cvGeneratorBO.DataManager')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('skillset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cvGeneratorBO.Skillset')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('company', models.TextField()),
                ('periode', models.TextField()),
                ('city', models.TextField()),
                ('description', models.TextField()),
                ('dataManager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cvGeneratorBO.DataManager')),
            ],
        ),
        migrations.AddField(
            model_name='datamanager',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cvGeneratorBO.Site'),
        ),
    ]
