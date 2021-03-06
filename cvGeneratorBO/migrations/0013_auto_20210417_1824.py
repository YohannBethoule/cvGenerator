# Generated by Django 3.0.3 on 2021-04-17 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cvGeneratorBO', '0012_info_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='dataManager',
        ),
        migrations.RemoveField(
            model_name='job',
            name='dataManager',
        ),
        migrations.RemoveField(
            model_name='project',
            name='dataManager',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='dataManager',
        ),
        migrations.RemoveField(
            model_name='skillset',
            name='dataManager',
        ),
        migrations.RemoveField(
            model_name='training',
            name='dataManager',
        ),
        migrations.AddField(
            model_name='info',
            name='site',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='infos', to='cvGeneratorBO.Site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='cvGeneratorBO.Site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='cvGeneratorBO.Site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='urlName',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='site',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='siteSettings', to='cvGeneratorBO.Site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillset',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='skillsets', to='cvGeneratorBO.Site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='training',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='trainings', to='cvGeneratorBO.Site'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DataManager',
        ),
    ]
