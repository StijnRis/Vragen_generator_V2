# Generated by Django 4.2 on 2023-04-06 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_rename_number_examination_page_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='text',
        ),
    ]
