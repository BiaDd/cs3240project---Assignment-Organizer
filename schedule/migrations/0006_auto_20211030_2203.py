# Generated by Django 3.2.7 on 2021-10-31 02:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20211029_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 31, 2, 3, 55, 159615, tzinfo=utc), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 31, 2, 3, 55, 159641, tzinfo=utc), verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='date_enrolled',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 31, 2, 3, 55, 160739, tzinfo=utc), verbose_name='date joined'),
        ),
    ]
