# Generated by Django 2.0.9 on 2018-10-09 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_auto_20181008_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('callstr', models.CharField(blank=True, max_length=25)),
                ('callbtn', models.CharField(blank=True, max_length=25)),
                ('callactn', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='webpage',
            name='calltoaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.CallToAction'),
        ),
    ]
