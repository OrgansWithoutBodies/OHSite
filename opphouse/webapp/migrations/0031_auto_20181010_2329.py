# Generated by Django 2.0.9 on 2018-10-11 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0030_auto_20181010_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donatepage',
            name='template_string',
        ),
        migrations.AddField(
            model_name='contactpage',
            name='baseurl',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='callactn',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='callbtn',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='callstr',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='headerimg',
            field=models.ImageField(blank=True, upload_to='headerimages/'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='headersubtitle',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='headertitle',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='tabname',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='eventspage',
            name='baseurl',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='eventspage',
            name='callactn',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='eventspage',
            name='callbtn',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='eventspage',
            name='callstr',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='eventspage',
            name='headerimg',
            field=models.ImageField(blank=True, upload_to='headerimages/'),
        ),
        migrations.AddField(
            model_name='eventspage',
            name='headersubtitle',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='eventspage',
            name='headertitle',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='eventspage',
            name='tabname',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='homepage',
            name='baseurl',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='homepage',
            name='callactn',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='callbtn',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='homepage',
            name='callstr',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='homepage',
            name='headerimg',
            field=models.ImageField(blank=True, upload_to='headerimages/'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='headersubtitle',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='homepage',
            name='headertitle',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='tabname',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='thriftpage',
            name='baseurl',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='thriftpage',
            name='callactn',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='thriftpage',
            name='callbtn',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='thriftpage',
            name='callstr',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='thriftpage',
            name='headerimg',
            field=models.ImageField(blank=True, upload_to='headerimages/'),
        ),
        migrations.AddField(
            model_name='thriftpage',
            name='headersubtitle',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='thriftpage',
            name='headertitle',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='thriftpage',
            name='tabname',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='wheelsforhopepage',
            name='baseurl',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='wheelsforhopepage',
            name='callactn',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='wheelsforhopepage',
            name='callbtn',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='wheelsforhopepage',
            name='callstr',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='wheelsforhopepage',
            name='headerimg',
            field=models.ImageField(blank=True, upload_to='headerimages/'),
        ),
        migrations.AddField(
            model_name='wheelsforhopepage',
            name='headersubtitle',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='wheelsforhopepage',
            name='headertitle',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='wheelsforhopepage',
            name='tabname',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
