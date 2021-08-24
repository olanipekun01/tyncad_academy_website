from django.db import models
from django.conf import settings
from django.utils import timezone

class Banner(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name