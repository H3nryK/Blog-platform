from django.db import models
from django.utils import timezone

class Blogs(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='media')
    uploaded_on = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title