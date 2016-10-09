# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 02:13
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckingAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('routing_number', models.IntegerField(unique=True)),
                ('current_balance', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('active_balance', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('creditcard_number', models.CharField(max_length=16, unique=True, validators=[django.core.validators.MinLengthValidator(16)])),
                ('charge_limit', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('remaining_credit', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('late_fee', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(15.0)])),
                ('days_late', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExternalCriticalTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('type_of_transaction', models.CharField(max_length=200)),
                ('time_resolved', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField()),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='externalcriticaltransaction_initiator', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='externalcriticaltransaction_participants', to=settings.AUTH_USER_MODEL)),
                ('resolver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='externalcriticaltransaction_resolver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExternalNoncriticalTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('type_of_transaction', models.CharField(max_length=200)),
                ('time_resolved', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField()),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='externalnoncriticaltransaction_initiator', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='externalnoncriticaltransaction_participants', to=settings.AUTH_USER_MODEL)),
                ('resolver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='externalnoncriticaltransaction_resolver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndividualCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('email', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('street_address', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)])),
                ('city', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('zipcode', models.CharField(max_length=5, validators=[django.core.validators.MinLengthValidator(5)])),
                ('session_key', models.CharField(max_length=100)),
                ('otp_pass', models.CharField(default='', max_length=13, validators=[django.core.validators.MinLengthValidator(13)])),
                ('otp_timestamp', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('trusted_device_keys', models.CharField(default='', max_length=110)),
                ('certificate', models.TextField(null=True)),
                ('ssn', models.CharField(max_length=9, unique=True, validators=[django.core.validators.MinLengthValidator(9)])),
                ('checking_account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='external.CheckingAccount')),
                ('credit_card', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='external.CreditCard')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MerchantOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('email', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('street_address', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)])),
                ('city', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('zipcode', models.CharField(max_length=5, validators=[django.core.validators.MinLengthValidator(5)])),
                ('session_key', models.CharField(max_length=100)),
                ('otp_pass', models.CharField(default='', max_length=13, validators=[django.core.validators.MinLengthValidator(13)])),
                ('otp_timestamp', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('trusted_device_keys', models.CharField(default='', max_length=110)),
                ('certificate', models.TextField(null=True)),
                ('business_code', models.CharField(max_length=9, unique=True, validators=[django.core.validators.MinLengthValidator(9)])),
                ('checking_account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='external.CheckingAccount')),
                ('credit_card', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='external.CreditCard')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MerchantPaymentRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchantCheckingsAccountNum', models.IntegerField()),
                ('accountType', models.CharField(max_length=30)),
                ('clientAccountNum', models.IntegerField()),
                ('clientRoutingNum', models.IntegerField()),
                ('requestAmount', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
            ],
        ),
        migrations.CreateModel(
            name='SavingsAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('routing_number', models.IntegerField(unique=True)),
                ('current_balance', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('active_balance', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='merchantorganization',
            name='savings_account',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='external.SavingsAccount'),
        ),
        migrations.AddField(
            model_name='merchantorganization',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='individualcustomer',
            name='savings_account',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='external.SavingsAccount'),
        ),
        migrations.AddField(
            model_name='individualcustomer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
