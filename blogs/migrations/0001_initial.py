# Generated by Django 4.2 on 2024-03-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('picture', models.ImageField(upload_to='media')),
                ('uploade_on', models.DateTimeField()),
                ('content', models.TextField()),
            ],
        ),
    ]
