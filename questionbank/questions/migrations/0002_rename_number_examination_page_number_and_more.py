# Generated by Django 4.2 on 2023-04-06 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examination',
            old_name='number',
            new_name='page_number',
        ),
        migrations.RenameField(
            model_name='examination',
            old_name='page',
            new_name='question_number',
        ),
    ]