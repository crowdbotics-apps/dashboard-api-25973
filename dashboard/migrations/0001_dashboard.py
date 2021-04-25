# Generated by Django 2.2.20 on 2021-04-25 17:47

import dashboard.models.choices
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[(dashboard.models.choices.AppTypeChoices('Web'), 'Web'), (dashboard.models.choices.AppTypeChoices('Mobile'), 'Mobile')], max_length=6)),
                ('framework', models.CharField(choices=[(dashboard.models.choices.AppFrameWorkChoices('Django'), 'Django'), (dashboard.models.choices.AppFrameWorkChoices('React Native'), 'React Native')], max_length=12)),
                ('domain_name', models.CharField(max_length=50)),
                ('screenshot', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('app', models.OneToOneField(on_delete=django.db.models.expressions.Case, to='dashboard.App')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='dashboard.Plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='plan',
            constraint=models.CheckConstraint(check=models.Q(name__length__gte=1), name='%(app_label)s_%(class)s_name_length'),
        ),
        migrations.AddConstraint(
            model_name='plan',
            constraint=models.CheckConstraint(check=models.Q(description__length__gte=1), name='%(app_label)s_%(class)s_description_length'),
        ),
        migrations.AddField(
            model_name='app',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apps', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='app',
            constraint=models.CheckConstraint(check=models.Q(name__length__gte=1), name='%(app_label)s_%(class)s_name_length'),
        ),
    ]
