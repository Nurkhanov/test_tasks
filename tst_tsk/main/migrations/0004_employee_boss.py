# Generated by Django 3.2.8 on 2022-05-03 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220503_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='boss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.employee'),
        ),
    ]
