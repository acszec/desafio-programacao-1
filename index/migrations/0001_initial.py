# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchaser_name', models.CharField(max_length=100)),
                ('item_description', models.CharField(max_length=100)),
                ('item_price', models.FloatField()),
                ('purchase_count', models.IntegerField()),
                ('merchant_address', models.CharField(max_length=100)),
                ('merchant_name', models.CharField(max_length=100)),
            ],
        ),
    ]
