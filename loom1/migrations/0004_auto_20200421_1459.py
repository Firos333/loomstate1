# Generated by Django 3.0.4 on 2020-04-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loom1', '0003_auto_20200419_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='faulttable',
            name='time_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='mastertable',
            name='time_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
