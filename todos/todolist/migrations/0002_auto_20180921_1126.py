# Generated by Django 2.1.1 on 2018-09-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='content',
            field=models.TextField(default='This is the default content'),
        ),
    ]
