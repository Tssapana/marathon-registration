from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='event_thumbnails/',null=True, blank= True)

    def __str__(self):
        return self.title

