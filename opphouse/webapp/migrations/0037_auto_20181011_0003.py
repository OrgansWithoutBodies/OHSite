# Generated by Django 2.0.9 on 2018-10-11 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0036_auto_20181010_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='callactn',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='callbtn',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='callstr',
        ),
        migrations.RemoveField(
            model_name='donatepage',
            name='callactn',
        ),
        migrations.RemoveField(
            model_name='donatepage',
            name='callbtn',
        ),
        migrations.RemoveField(
            model_name='donatepage',
            name='callstr',
        ),
        migrations.RemoveField(
            model_name='eventspage',
            name='callactn',
        ),
        migrations.RemoveField(
            model_name='eventspage',
            name='callbtn',
        ),
        migrations.RemoveField(
            model_name='eventspage',
            name='callstr',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='callactn',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='callbtn',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='callstr',
        ),
        migrations.RemoveField(
            model_name='thriftpage',
            name='callactn',
        ),
        migrations.RemoveField(
            model_name='thriftpage',
            name='callbtn',
        ),
        migrations.RemoveField(
            model_name='thriftpage',
            name='callstr',
        ),
        migrations.RemoveField(
            model_name='volunteerpage',
            name='callactn',
        ),
        migrations.RemoveField(
            model_name='volunteerpage',
            name='callbtn',
        ),
        migrations.RemoveField(
            model_name='volunteerpage',
            name='callstr',
        ),
        migrations.RemoveField(
            model_name='wheelsforhopepage',
            name='callactn',
        ),
        migrations.RemoveField(
            model_name='wheelsforhopepage',
            name='callbtn',
        ),
        migrations.RemoveField(
            model_name='wheelsforhopepage',
            name='callstr',
        ),
    ]