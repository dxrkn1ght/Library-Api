# Generated by Django 5.1.7 on 2025-03-06 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcopy',
            options={'ordering': ['added_date'], 'verbose_name_plural': 'copies'},
        ),
    ]
