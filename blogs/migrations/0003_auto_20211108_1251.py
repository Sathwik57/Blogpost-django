# Generated by Django 3.2.9 on 2021-11-08 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blogs_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogs',
            new_name='Blog',
        ),
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]