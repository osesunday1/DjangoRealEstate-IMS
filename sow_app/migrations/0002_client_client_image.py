# Generated by Django 4.1.7 on 2023-03-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sow_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
