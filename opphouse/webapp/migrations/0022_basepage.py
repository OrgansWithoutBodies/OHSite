# Generated by Django 2.0.9 on 2018-10-09 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('webapp', '0021_auto_20181008_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headerimg', models.ImageField(blank=True, upload_to='headerimages/')),
                ('tabname', models.CharField(blank=True, max_length=20)),
                ('url', models.CharField(blank=True, max_length=20)),
                ('headertitle', models.CharField(blank=True, max_length=50)),
                ('headersubtitle', models.CharField(blank=True, max_length=80)),
                ('callstr', models.CharField(blank=True, max_length=25)),
                ('callbtn', models.CharField(blank=True, max_length=25)),
                ('callactn', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]