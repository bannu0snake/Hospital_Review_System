# Generated by Django 3.1.5 on 2021-04-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0005_hospital_ratings_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='non_stars',
            field=models.CharField(default='12345', max_length=5),
        ),
    ]