# Generated by Django 3.2.9 on 2021-12-15 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plan', '0001_initial'),
        ('shortener', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenedurls',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organization',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='plan.plan'),
        ),
        migrations.AddField(
            model_name='categories',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categories',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shortener.organization'),
        ),
        migrations.AddIndex(
            model_name='shortenedurls',
            index=models.Index(fields=['prefix', 'shortened_url'], name='shortener_s_prefix_bbcd1e_idx'),
        ),
    ]
