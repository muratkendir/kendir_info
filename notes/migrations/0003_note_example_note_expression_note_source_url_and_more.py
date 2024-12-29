# Generated by Django 5.1.3 on 2024-12-28 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_notes_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='example',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='note',
            name='expression',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='note',
            name='source_url',
            field=models.URLField(default='none', max_length=511),
        ),
        migrations.AddField(
            model_name='note',
            name='type',
            field=models.CharField(choices=[('gnrl', 'General'), ('prsn', 'Personal'), ('Trck', 'Trick')], default='gnrl', max_length=15),
        ),
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(default='none'),
        ),
    ]