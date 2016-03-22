# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('title_ko', models.CharField(db_index=True, max_length=100, null=True)),
                ('title_en', models.CharField(db_index=True, max_length=100, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('desc_ko', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
                ('announce_after', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='EmailToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('token', models.CharField(max_length=64, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('organization', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'speaker')),
                ('bio', models.TextField(blank=True, max_length=4000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('name_ko', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_en', models.CharField(db_index=True, max_length=100, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('desc_ko', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
                ('slide_url', models.CharField(blank=True, max_length=255, null=True)),
                ('pdf_url', models.CharField(blank=True, max_length=255, null=True)),
                ('video_url', models.CharField(blank=True, max_length=255, null=True)),
                ('language', models.CharField(choices=[(b'ko', b'Korean'), (b'en', b'English')], default=b'ko', max_length=2)),
                ('is_recordable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('name_ko', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_en', models.CharField(db_index=True, max_length=100, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgramTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_ko', models.CharField(max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('begin', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('brief', models.TextField(max_length=1000)),
                ('desc', models.TextField(max_length=4000)),
                ('comment', models.TextField(blank=True, max_length=4000, null=True)),
                ('difficulty', models.CharField(choices=[(b'B', 'Beginner'), (b'I', 'Intermediate'), (b'E', 'Experienced')], max_length=1)),
                ('duration', models.CharField(choices=[(b'S', '25 mins'), (b'L', '40 mins')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_uid', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('transaction_code', models.CharField(max_length=36)),
                ('payment_method', models.CharField(choices=[(b'card', '\uc2e0\uc6a9\uce74\ub4dc')], default=b'card', max_length=20)),
                ('payment_status', models.CharField(max_length=10)),
                ('payment_message', models.CharField(max_length=255, null=True)),
                ('vbank_num', models.CharField(blank=True, max_length=255, null=True)),
                ('vbank_name', models.CharField(blank=True, max_length=20, null=True)),
                ('vbank_date', models.CharField(blank=True, max_length=50, null=True)),
                ('vbank_holder', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_ko', models.CharField(max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('desc_ko', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('name_ko', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_en', models.CharField(db_index=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'speaker')),
                ('desc', models.TextField(blank=True, null=True)),
                ('desc_ko', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
                ('info', jsonfield.fields.JSONField(blank=True, default=dict, help_text='help-text-for-speaker-info')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('name_ko', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_en', models.CharField(db_index=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'sponsor')),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('desc_ko', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SponsorLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('name_ko', models.CharField(db_index=True, max_length=100, null=True)),
                ('name_en', models.CharField(db_index=True, max_length=100, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('desc_ko', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='sponsor',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pyconkr.SponsorLevel'),
        ),
        migrations.AddField(
            model_name='program',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pyconkr.ProgramCategory'),
        ),
        migrations.AddField(
            model_name='program',
            name='date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pyconkr.ProgramDate'),
        ),
        migrations.AddField(
            model_name='program',
            name='rooms',
            field=models.ManyToManyField(blank=True, to='pyconkr.Room'),
        ),
        migrations.AddField(
            model_name='program',
            name='speakers',
            field=models.ManyToManyField(blank=True, to='pyconkr.Speaker'),
        ),
        migrations.AddField(
            model_name='program',
            name='times',
            field=models.ManyToManyField(blank=True, to='pyconkr.ProgramTime'),
        ),
    ]
