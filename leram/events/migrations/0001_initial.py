# Generated by Django 3.1.8 on 2021-04-22 18:59

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_resized.forms
import leram.events.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Event/Destination Title')),
                ('location', models.CharField(max_length=400, null=True, verbose_name='Event/Destination Location')),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1920, 1148], upload_to=leram.events.models.events_file_path, verbose_name='Upload Event/Destination Image')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Destination Travel Expenses')),
                ('pub_date', models.DateField(null=True, verbose_name='Event/Destination Published Date')),
                ('event_date', models.DateTimeField(null=True, verbose_name='Event/Destination Date & Time')),
                ('content', ckeditor.fields.RichTextField(verbose_name='About the Event/Destination')),
                ('map_lat', models.CharField(help_text='Google online for the latitude of the location to get an accurate readding here. https://map.google.com', max_length=7, null=True, verbose_name='Map Latitude')),
                ('map_lng', models.CharField(help_text='Google online for the longitude of the location to get an accurate readding here. https://map.google.com', max_length=7, null=True, verbose_name='Map Longitude')),
                ('registration', models.BooleanField(default=False, verbose_name='Application Closed')),
                ('booked', models.BooleanField(default=False, verbose_name='Have you booked')),
                ('featured', models.BooleanField(default=False, verbose_name='Featured Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]