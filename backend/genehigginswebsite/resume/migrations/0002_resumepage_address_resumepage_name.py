# Generated by Django 4.0 on 2022-08-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumepage',
            name='address',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='resumepage',
            name='name',
            field=models.TextField(default='Bozo', max_length=250),
            preserve_default=False,
        ),
    ]
