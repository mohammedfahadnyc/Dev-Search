# Generated by Django 4.1.5 on 2023-02-06 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_featured_image_alter_project_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='vote_ration',
            new_name='vote_ratio',
        ),
    ]
