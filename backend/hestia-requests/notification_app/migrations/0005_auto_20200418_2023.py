# Generated by Django 2.2 on 2020-04-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification_app', '0004_userfcmdevice_date_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfcmdevice',
            name='registration_id',
            field=models.TextField(),
        ),
    ]
