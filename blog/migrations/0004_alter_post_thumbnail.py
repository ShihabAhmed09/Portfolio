# Generated by Django 3.2.5 on 2021-08-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='blog/thumbnails/thumbnail.png', upload_to='blog/thumbnails'),
        ),
    ]