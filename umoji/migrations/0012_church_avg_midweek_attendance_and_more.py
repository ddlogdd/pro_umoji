# Generated by Django 4.0.6 on 2023-03-19 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umoji', '0011_church_edited_kap_edited_managementreport_edited_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='avg_midweek_attendance',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='highest_midweek_attendance',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='total_midweek_attendance',
            field=models.IntegerField(null=True),
        ),
    ]
