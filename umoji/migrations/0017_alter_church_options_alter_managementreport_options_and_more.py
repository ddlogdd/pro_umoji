# Generated by Django 4.0.5 on 2023-03-20 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umoji', '0016_alter_managementreport_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='church',
            options={'permissions': [('pastor', 'Can acess pastor'), ('pastor alone', 'only pastor')]},
        ),
        migrations.AlterModelOptions(
            name='managementreport',
            options={'permissions': [('elder', 'for cmc'), ('access', 'can access cmc')]},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'permissions': [('media', 'for media')]},
        ),
        migrations.AlterModelOptions(
            name='servicereport',
            options={'permissions': [('ushers', 'for ushers')]},
        ),
    ]
