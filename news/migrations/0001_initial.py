# Generated by Django 3.2 on 2021-05-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('summary', models.CharField(max_length=600)),
                ('published_date', models.CharField(max_length=15)),
                ('url', models.CharField(max_length=500)),
                ('source', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('short_name', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=100)),
                ('rss_link', models.CharField(max_length=100)),
            ],
        ),
    ]
