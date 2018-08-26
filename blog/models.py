# posts/models.py
from django.db import models
from datetime import datetime

class Blog(models.Model):
    blog_title = models.CharField(max_length=200,default="", blank=False)
    content = models.TextField()
    author = models.CharField(max_length=100,default="", blank=True)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        """A string representation of the model."""
        return self.blog_title[:50]