from django.db import models
from django.conf import settings
from django.utils import timezone

class Banner(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    banner = models.FileField(upload_to='banners', null=True, blank=True, default='')
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class ContactUs(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500, blank=True, null=True, default='')
    phone_number = models.CharField(max_length=50)
    description = models.TextField()
    is_contacted = models.BooleanField(default=True)
    time_contacted = models.DateTimeField(default='', blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    