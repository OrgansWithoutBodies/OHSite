# Generated by Django 2.1.1 on 2018-10-03 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20181002_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='headerimg',
            field=models.ImageField(upload_to='headerimages/'),
        ),
    ]
