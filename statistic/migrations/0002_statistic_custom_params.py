# Generated by Django 3.2.9 on 2021-12-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='custom_params',
            field=models.JSONField(null=True),
        ),
    ]