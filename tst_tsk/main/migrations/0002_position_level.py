# Generated by Django 4.0.4 on 2022-04-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
