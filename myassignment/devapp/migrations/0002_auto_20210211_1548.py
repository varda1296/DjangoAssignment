# Generated by Django 2.2.18 on 2021-02-11 10:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('devapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityperiods',
            name='User',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='devapp.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activityperiods',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
