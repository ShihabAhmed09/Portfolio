# Generated by Django 3.2.5 on 2021-08-04 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='users/profile_pics/default.jpg', upload_to='users/profile_pics'),
        ),
    ]