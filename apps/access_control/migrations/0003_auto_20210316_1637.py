# Generated by Django 3.1.7 on 2021-03-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_control', '0002_useraccount_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='hire_date',
            field=models.DateField(null=True),
        ),
    ]
