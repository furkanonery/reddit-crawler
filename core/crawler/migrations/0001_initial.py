# Generated by Django 4.2.2 on 2023-06-19 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubredditPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('created_utc', models.DateTimeField()),
                ('url', models.URLField()),
                ('subreddit', models.CharField(max_length=100)),
            ],
        ),
    ]
