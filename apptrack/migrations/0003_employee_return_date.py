# Generated by Django 4.2.1 on 2023-08-10 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptrack', '0002_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='return_date',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
