# Generated by Django 3.2.9 on 2022-03-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shrink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_link', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
    ]