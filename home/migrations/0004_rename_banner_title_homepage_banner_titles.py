# Generated by Django 4.0.3 on 2022-03-02 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_banner_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='banner_title',
            new_name='banner_titles',
        ),
    ]
