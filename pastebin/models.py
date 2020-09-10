from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Paste(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=40, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name or str(self.id)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pastebin_paste_detail', args=[str(self.id)])
    
    
    