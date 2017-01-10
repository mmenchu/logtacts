# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-09 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0027_auto_20170106_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookowner',
            name='check_foursquare',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bookowner',
            name='check_twitter_dms',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bookowner',
            name='check_twitter_mentions',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bookowner',
            name='send_birthday_reminders',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookowner',
            name='send_contact_reminders',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalbookowner',
            name='check_foursquare',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalbookowner',
            name='check_twitter_dms',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalbookowner',
            name='check_twitter_mentions',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalbookowner',
            name='send_birthday_reminders',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalbookowner',
            name='send_contact_reminders',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='plan',
            field=models.CharField(blank=True, choices=[('basic_monthly', 'Basic Monthly Subscription'), ('team_monthly', 'Team Monthly Subscription'), ('family_monthly', 'Family Monthly Subscription'), ('team_yearly', 'Team Yearly Subscription'), ('basic_yearly', 'Basic Yearly Subscription'), ('family_yearly', 'Family Yearly Subscription')], max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalbook',
            name='plan',
            field=models.CharField(blank=True, choices=[('basic_monthly', 'Basic Monthly Subscription'), ('team_monthly', 'Team Monthly Subscription'), ('family_monthly', 'Family Monthly Subscription'), ('team_yearly', 'Team Yearly Subscription'), ('basic_yearly', 'Basic Yearly Subscription'), ('family_yearly', 'Family Yearly Subscription')], max_length=100),
        ),
    ]
