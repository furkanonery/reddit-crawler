from django.db import models

class Subreddits(models.Model):
    title = models.CharField(max_length=255)
    subreddit = models.CharField(max_length=100)

    def __str__(self):
        return self.title
