# Generated by Django 2.2.7 on 2019-11-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0019_clinics_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='question',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
