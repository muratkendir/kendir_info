# Generated by Django 5.1.3 on 2025-01-03 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_alter_note_options_alter_note_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='list',
            new_name='list_id',
        ),
    ]
