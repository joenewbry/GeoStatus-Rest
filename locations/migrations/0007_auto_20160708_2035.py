# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 20:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_remove_context_context'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='name',
        ),
        migrations.AddField(
            model_name='status',
            name='context',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='status_context', to='locations.Context'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='context',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='context_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='status',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]