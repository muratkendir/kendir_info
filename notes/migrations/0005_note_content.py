# Generated by Django 5.1.3 on 2024-12-29 00:18

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_note_source_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='content',
            field=markdownx.models.MarkdownxField(blank=True),
        ),
    ]