# Generated by Django 3.2.11 on 2024-09-10 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdetail',
            name='name_copy',
        ),
    ]
