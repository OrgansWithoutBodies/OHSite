# Generated by Django 2.1.1 on 2018-09-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventname',
            field=models.CharField(default='Cocktails for a cause', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pickup',
            name='imgs',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='pickup',
            name='items',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donor',
            name='otherinfo',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pickup',
            name='specinstruct',
            field=models.TextField(blank=True),
        ),
    ]