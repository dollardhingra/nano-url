# Generated by Django 3.2.6 on 2021-08-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0002_alter_url_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_name',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
