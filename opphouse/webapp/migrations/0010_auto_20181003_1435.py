# Generated by Django 2.1.1 on 2018-10-03 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20181003_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]