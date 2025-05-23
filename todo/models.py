from django.db import models

# Create your models here.
class saqme(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ImageField(blank=True, null=True)
    description = models.CharField(blank=True, null=True, max_length=255)
    