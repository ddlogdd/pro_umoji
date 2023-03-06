# Generated by Django 4.0.6 on 2023-03-05 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Umoji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('wsf_prayers', models.TextField()),
                ('wsf_outline', models.TextField()),
                ('Income_report', models.TextField()),
                ('service_unit', models.CharField(max_length=40)),
                ('message_title', models.CharField(max_length=40)),
                ('service_sequence', models.CharField(max_length=3)),
                ('number_of_males', models.CharField(max_length=10)),
                ('number_of_females', models.CharField(max_length=10)),
                ('number_of_children', models.CharField(max_length=10)),
                ('number_of_first_timers', models.CharField(max_length=10)),
                ('number_of_new_converts', models.CharField(max_length=10)),
                ('number_of_cars', models.CharField(max_length=10)),
                ('Total_attendace', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
