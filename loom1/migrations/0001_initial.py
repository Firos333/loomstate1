# Generated by Django 3.0.4 on 2020-04-19 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaultTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unique_id', models.CharField(default=0, max_length=50)),
                ('meter', models.IntegerField(default=0)),
                ('fault', models.CharField(default=0, max_length=50)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unique_id', models.CharField(default=0, max_length=50, unique=True)),
                ('loom_no', models.CharField(default=0, max_length=50)),
                ('set_no', models.IntegerField(default=0)),
                ('beam_no', models.IntegerField(default=0)),
                ('piece_no', models.IntegerField(default=0)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
