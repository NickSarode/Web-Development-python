# Generated by Django 4.0.3 on 2022-03-13 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoteldetails',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='hoteldetails',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='hoteldetails',
            name='position',
        ),
        migrations.RemoveField(
            model_name='hoteldetails',
            name='title',
        ),
        migrations.AddField(
            model_name='hoteldetails',
            name='fb_profile',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hoteldetails',
            name='website',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]