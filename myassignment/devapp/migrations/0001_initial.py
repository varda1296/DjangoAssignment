# Generated by Django 2.2.18 on 2021-02-11 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=100)),
                ('tz', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriods',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='devapp.User')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]
