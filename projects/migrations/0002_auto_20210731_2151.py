# Generated by Django 3.2.5 on 2021-07-31 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['-knowledge']},
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='projects.Tag'),
        ),
    ]