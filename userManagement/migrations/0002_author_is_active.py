# Generated by Django 5.0.4 on 2024-06-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]