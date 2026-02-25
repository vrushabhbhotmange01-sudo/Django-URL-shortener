from django.db import models
from django.utils import timezone

class URLSTORAGE(models.Model):
    original_url= models.CharField()
    short_code= models.CharField(max_length=12)
    created_at= models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True,null=True)
    click_count= models.IntegerField(default=0)
    class Meta:
        indexes = [models.Index(fields = ['short_code'])]
    def is_expired(self):
        return self.expires_at and timezone.now()>self.expires_at
    