# Generated by Django 2.1.1 on 2018-10-02 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_event_eventdesc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headerimg', models.ImageField(upload_to='')),
                ('tabname', models.CharField(max_length=20)),
                ('menuname', models.CharField(max_length=10)),
                ('headertitle', models.CharField(max_length=50)),
                ('headersubtitle', models.CharField(blank=True, max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='img',
            field=models.ImageField(blank=True, upload_to='eventimages/'),
        ),
        migrations.AlterField(
            model_name='pickup',
            name='imgs',
            field=models.ImageField(blank=True, upload_to='uploadedimages/'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='pic',
            field=models.ImageField(blank=True, upload_to='sponsorimages/'),
        ),
    ]
