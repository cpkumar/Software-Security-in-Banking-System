# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 19:58
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('external', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('email', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('street_address', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)])),
                ('city', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('zipcode', models.IntegerField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(5)])),
                ('session_key', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InternalCriticalTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('type_of_transaction', models.CharField(max_length=200)),
                ('time_resolved', models.DateTimeField(auto_now_add=True)),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internalcriticaltransaction_initiator', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='internalcriticaltransaction_participants', to=settings.AUTH_USER_MODEL)),
                ('resolver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internalcriticaltransaction_resolver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InternalNoncriticalTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('type_of_transaction', models.CharField(max_length=200)),
                ('time_resolved', models.DateTimeField(auto_now_add=True)),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internalnoncriticaltransaction_initiator', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='internalnoncriticaltransaction_participants', to=settings.AUTH_USER_MODEL)),
                ('resolver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internalnoncriticaltransaction_resolver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegularEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('email', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('street_address', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)])),
                ('city', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('zipcode', models.IntegerField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(5)])),
                ('session_key', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SystemManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('email', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('street_address', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)])),
                ('city', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('zipcode', models.IntegerField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(5)])),
                ('session_key', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_critical_transaction', models.ManyToManyField(to='external.ExternalCriticalTransaction')),
                ('external_noncritical_transaction', models.ManyToManyField(to='external.ExternalNoncriticalTransaction')),
                ('internal_critical_transaction', models.ManyToManyField(to='internal.InternalCriticalTransaction')),
                ('internal_noncritical_transaction', models.ManyToManyField(to='internal.InternalNoncriticalTransaction')),
            ],
        ),
    ]
