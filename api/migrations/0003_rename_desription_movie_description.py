# Generated by Django 4.1.7 on 2023-04-25 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_character_movieid_alter_rating_movieid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='desription',
            new_name='description',
        ),
    ]
