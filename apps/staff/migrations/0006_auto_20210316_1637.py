# Generated by Django 3.1.7 on 2021-03-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mission', models.CharField(max_length=500)),
                ('relationship', models.CharField(blank=True, choices=[('child', 'Child'), ('husband', 'Husband'), ('wife', 'Wife')], max_length=70)),
            ],
        ),
        migrations.DeleteModel(
            name='StaffProfile',
        ),
    ]
