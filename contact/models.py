from django.db import models

# Create your models here.

class contact_us(models.Model):
    contact_name = models.CharField(max_length=100,blank=False)
    contact_email = models.CharField(max_length=100,blank=False)
    contact_subject = models.TextField(max_length=200,blank=False)
    contact_message = models.TextField(max_length=700,blank=False)
    

    def __str__(self):
        return self.contact_subject
