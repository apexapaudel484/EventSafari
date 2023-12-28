# Generated by Django 4.2.6 on 2023-12-28 02:45

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attendee',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Organizer', 'ORGANIZER'), ('Audience', 'AUDIENCE')], default=[], max_length=20, null=True),
        ),
    ]
