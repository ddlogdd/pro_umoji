# Generated by Django 4.0.6 on 2023-03-13 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umoji', '0004_alter_managementreport_total_attendace_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managementreport',
            name='Total_attendace',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='managementreport',
            name='number_of_cars',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='managementreport',
            name='number_of_children',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='managementreport',
            name='number_of_females',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='managementreport',
            name='number_of_first_timers',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='managementreport',
            name='number_of_males',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='managementreport',
            name='number_of_new_converts',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='managementreport',
            name='service_sequence',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='servicereport',
            name='Total_attendace',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='servicereport',
            name='number_of_cars',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='servicereport',
            name='number_of_children',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='servicereport',
            name='number_of_females',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='servicereport',
            name='number_of_first_timers',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='servicereport',
            name='number_of_males',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='servicereport',
            name='number_of_new_converts',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='servicereport',
            name='service_sequence',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wsfleaders',
            name='Total_attendace',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wsfleaders',
            name='number_of_children',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wsfleaders',
            name='number_of_females',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wsfleaders',
            name='number_of_first_timers',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wsfleaders',
            name='number_of_males',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wsfleaders',
            name='number_of_new_converts',
            field=models.IntegerField(),
        ),
    ]
