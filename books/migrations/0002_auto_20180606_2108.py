# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-06 21:08
from __future__ import unicode_literals

import django.contrib.auth.validators
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location=b'/home/zeynelabidin/myGit/bookworm/media'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location=b'/home/zeynelabidin/myGit/bookworm/media'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='known_words_file',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location=b'/home/zeynelabidin/myGit/bookworm/media'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
    ]