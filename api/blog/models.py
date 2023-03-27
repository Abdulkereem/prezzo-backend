from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
import uuid

class Blog(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    article = RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']


    def __str__(self):
        return self.title
    

