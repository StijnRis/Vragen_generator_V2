# Generated by Django 4.2 on 2023-04-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_rename_question_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='pdf_path',
            field=models.FilePathField(default=''),
            preserve_default=False,
        ),
    ]
