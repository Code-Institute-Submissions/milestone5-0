# Generated by Django 3.1 on 2020-08-23 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourprograms', '0007_auto_20200823_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourprogram',
            name='date',
            field=models.CharField(max_length=254),
        ),
    ]
