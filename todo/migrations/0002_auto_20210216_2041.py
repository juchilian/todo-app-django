# Generated by Django 2.2 on 2021-02-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
