# Generated by Django 3.1 on 2020-08-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20200821_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='select_departure_date',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
