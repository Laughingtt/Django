# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-16 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_permission_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True),
        ),
    ]
