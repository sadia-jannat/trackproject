# Generated by Django 4.2.1 on 2023-08-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptrack', '0006_alter_employeeadd_options_alter_device_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeadd',
            name='return_date',
            field=models.TextField(max_length=100),
        ),
    ]
