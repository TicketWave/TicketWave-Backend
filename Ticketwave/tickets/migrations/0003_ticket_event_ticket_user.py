# Generated by Django 4.1 on 2023-04-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_remove_ticket_csvfile_ticket_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='event',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]