# Generated by Django 4.2.2 on 2023-07-09 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_soup', '0003_alter_subreddits_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubredditPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('vote', models.IntegerField()),
                ('author', models.CharField(max_length=255)),
                ('text', models.TextField(null=True)),
                ('img', models.CharField(max_length=255, null=True)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]