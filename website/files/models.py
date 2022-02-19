from django.db import models

class File(models.Model):
    
    date_created = models.DateTimeField(auto_now_add=True)
    file_url = models.URLField(null=True)
    file_name = models.CharField(max_length=200, null=True)
    file_extention = models.CharField(max_length=200, null=True)
    deleted = models.BooleanField(null=True, default=False)