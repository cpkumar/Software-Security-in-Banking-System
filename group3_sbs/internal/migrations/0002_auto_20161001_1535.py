# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 15:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='internalcriticaltransaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='internalnoncriticaltransaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]