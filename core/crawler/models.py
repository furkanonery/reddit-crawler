from django.db import models

class SubredditPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    created_utc = models.DateTimeField()
    url = models.URLField()
    subreddit = models.CharField(max_length=100)

    def __str__(self):
        return self.title
