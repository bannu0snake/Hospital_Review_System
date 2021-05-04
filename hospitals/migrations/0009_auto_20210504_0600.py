# Generated by Django 3.1.5 on 2021-05-04 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0008_auto_20210504_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='Achievements3',
            field=models.CharField(default='No Hospital information added recently', max_length=50),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Achievements4',
            field=models.CharField(default='No Hospital information added recently', max_length=50),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Achievements5',
            field=models.CharField(default='No Hospital information added recently', max_length=50),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Achievements6',
            field=models.CharField(default='No Hospital information added recently', max_length=50),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='ChiefMedicalOfficerPhoto',
            field=models.FileField(default='ChiefDoctorPhotos/doctt.png', upload_to='ChiefDoctorPhotos/'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='HospitalPhoto',
            field=models.FileField(default='HospitalPhotos/hospitalPhotos.jpg', upload_to='HospitalPhotos/'),
        ),
    ]
