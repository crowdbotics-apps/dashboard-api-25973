# Generated by Django 2.2.20 on 2021-04-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_dashboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
