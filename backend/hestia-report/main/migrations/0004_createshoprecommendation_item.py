# Generated by Django 3.0.4 on 2020-03-30 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200326_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='createshoprecommendation',
            name='item',
            field=models.CharField(default='sanitizer', max_length=30),
            preserve_default=False,
        ),
    ]