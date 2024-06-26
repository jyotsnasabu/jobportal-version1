# Generated by Django 5.0.4 on 2024-06-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0024_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermember',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usermember',
            name='resume',
            field=models.FileField(null=True, upload_to='resumes/'),
        ),
        migrations.AddField(
            model_name='usermember',
            name='user_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(null=True, upload_to='resumes/'),
        ),
    ]
