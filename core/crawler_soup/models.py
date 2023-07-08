from django.core.exceptions import ValidationError
from django.db import models

class Subreddits(models.Model):
    title = models.CharField(max_length=255)
    subreddit = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        existing_subreddits = Subreddits.objects.filter(title=self.title)
        if existing_subreddits.exists():
            return
        super().save(*args, **kwargs)
