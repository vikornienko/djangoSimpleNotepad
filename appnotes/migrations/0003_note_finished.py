# Generated by Django 4.1.2 on 2022-11-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnotes', '0002_note_due_date_note_note_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
