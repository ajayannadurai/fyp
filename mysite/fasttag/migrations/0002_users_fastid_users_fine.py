# Generated by Django 4.0.4 on 2022-05-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasttag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='fastid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='fine',
            field=models.IntegerField(default=0),
        ),
    ]