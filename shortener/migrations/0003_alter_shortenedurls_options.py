# Generated by Django 3.2.9 on 2021-12-03 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortenedurls',
            options={'ordering': ['-created_at']},
        ),
    ]
