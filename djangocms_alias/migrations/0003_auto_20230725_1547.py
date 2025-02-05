# Generated by Django 4.1.8 on 2023-07-25 15:47

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__latest__'),
        ('djangocms_alias', '0002_auto_20200723_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliasplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin'),
        ),
        migrations.AlterField(
            model_name='categorytranslation',
            name='name',
            field=models.CharField(max_length=120, verbose_name='name'),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together={('language_code', 'master'), ('name', 'language_code')},
        ),
    ]
