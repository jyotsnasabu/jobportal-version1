# Generated by Django 5.0.4 on 2024-05-31 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0014_remove_job_description_job_companyname_job_job_des_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='title',
        ),
    ]