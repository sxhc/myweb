from django.db import models
from django.utils import timezone

#creat models

class Post(models.Model):
    title = models.CharField(max_length=200)
    webadd = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        # ordering by pub_date
        ordering = ('-pub_date',)
    
    def __unicode__(self):
        # show title 
        return self.title