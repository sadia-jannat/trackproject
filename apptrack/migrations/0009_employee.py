# Generated by Django 4.2.1 on 2023-08-11 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptrack', '0008_remove_employeeadd_return_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('device_type', models.CharField(max_length=200)),
                ('device_name', models.CharField(max_length=200)),
                ('device_number', models.IntegerField()),
                ('handed_out', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50)),
                ('handed_date', models.DateField()),
                ('returned', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50)),
                ('returned_date', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employee',
            },
        ),
    ]
