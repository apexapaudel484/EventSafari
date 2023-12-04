# Generated by Django 4.2.6 on 2023-12-04 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=150)),
                ('event_description', models.TextField(blank=True, max_length=500)),
                ('event_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_location', models.CharField(default='Default Location', max_length=255)),
                ('event_capacity', models.IntegerField()),
                ('event_category', models.CharField(choices=[('Music and Dance', 'Music and Dance'), ('Sports', 'Sports'), ('Religious', 'Religious'), ('Yoga and Meditation', 'Yoga and Meditation'), ('Other', 'Other')], max_length=100, unique=True)),
                ('event_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('event_image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organizer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('booking_type', models.CharField(choices=[('Reserve Event', 'Reserve Event'), ('Buy Tickets', 'Buy Tickets')], max_length=40, unique=True)),
                ('ticket_quantity', models.IntegerField(default=1)),
                ('total_price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('audience_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
    ]
