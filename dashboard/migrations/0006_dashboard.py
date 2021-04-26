# Generated by Django 2.2.20 on 2021-04-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_dashboard'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='app',
            constraint=models.CheckConstraint(check=models.Q(type__in=['Web', 'Mobile']), name='%(app_label)s_%(class)s_type_valid'),
        ),
        migrations.AddConstraint(
            model_name='app',
            constraint=models.CheckConstraint(check=models.Q(framework__in=['Django', 'React Native']), name='%(app_label)s_%(class)s_framework_valid'),
        ),
        migrations.AddConstraint(
            model_name='plan',
            constraint=models.CheckConstraint(check=models.Q(price__in=['$0', '$10', '$25']), name='%(app_label)s_%(class)s_price_valid'),
        ),
        migrations.AddConstraint(
            model_name='plan',
            constraint=models.CheckConstraint(check=models.Q(name__in=['Free', 'Standard', 'Pro']), name='%(app_label)s_%(class)s_price_valid'),
        ),
    ]