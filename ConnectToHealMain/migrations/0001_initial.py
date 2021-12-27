# Generated by Django 3.2.7 on 2021-12-26 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=150)),
                ('date_published', models.DateField()),
                ('blog', models.TextField(default='')),
                ('cover', models.ImageField(default='default.jpg', upload_to='blogCovers')),
                ('link', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(max_length=255)),
            ],
        ),
    ]
