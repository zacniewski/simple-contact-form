# Generated by Django 4.2.2 on 2023-06-28 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['id']},
        ),
    ]
