# Generated by Django 2.2.7 on 2019-11-09 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0015_auto_20191109_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='notificated',
        ),
    ]