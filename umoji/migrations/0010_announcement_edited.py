# Generated by Django 4.0.6 on 2023-03-19 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umoji', '0009_alter_managementreport_total_attendace_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]