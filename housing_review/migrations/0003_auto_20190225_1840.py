# Generated by Django 2.1.5 on 2019-02-25 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housing_review', '0002_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='amenities_provided',
        ),
        migrations.RemoveField(
            model_name='review',
            name='parking',
        ),
        migrations.RemoveField(
            model_name='review',
            name='pets',
        ),
        migrations.RemoveField(
            model_name='review',
            name='pool',
        ),
        migrations.RemoveField(
            model_name='review',
            name='utilities_provided',
        ),
        migrations.AddField(
            model_name='review',
            name='amenities',
            field=models.CharField(blank=True, choices=[('parking', 'Parking'), ('pets', 'Pets'), ('pool', 'Pool')], max_length=3),
        ),
        migrations.AddField(
            model_name='review',
            name='utilities',
            field=models.CharField(blank=True, choices=[('electricity', 'Electricity'), ('water', 'Water'), ('internet', 'Internet')], max_length=3),
        ),
        migrations.AlterField(
            model_name='review',
            name='neighborhood',
            field=models.CharField(blank=True, choices=[('Wertland', 'Wertland'), ('Rugby', 'Rugby'), ('14th Street', '14th Street'), ('JPA', 'JPA'), ('Main Street', 'Main Street')], max_length=3),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='housing_review.User'),
        ),
    ]
