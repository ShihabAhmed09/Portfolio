# Generated by Django 3.2.5 on 2021-08-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default='projects/thumbnails/thumbnail.png', upload_to='projects/thumbnails'),
        ),
    ]
