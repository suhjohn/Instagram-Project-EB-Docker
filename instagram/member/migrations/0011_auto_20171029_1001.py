# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 10:01
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models
import member.custom_validators


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0010_auto_20171025_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', unique=True, verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=150, unique=True, validators=[member.custom_validators.validate_fb_username, django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
