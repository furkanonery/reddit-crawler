# Generated by Django 4.2.2 on 2023-07-08 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_soup', '0002_alter_subreddits_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subreddits',
            unique_together=set(),
        ),
    ]
