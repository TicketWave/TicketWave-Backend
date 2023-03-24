# Generated by Django 4.1.7 on 2023-03-21 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('short_name', models.CharField(max_length=18, unique=True)),
                ('resource_uri', models.URLField(null=True)),
                ('parent_category', models.IntegerField(null=True)),
            ],
        ),
    ]
