# Generated by Django 2.1.1 on 2018-10-02 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_sponsor_sponsortype'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]