# Generated by Django 2.1.5 on 2019-02-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_review', '0003_auto_20190225_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='amenities',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='review',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='review',
            name='utilities',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
