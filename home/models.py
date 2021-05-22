from django.db import models

# Create your models here.
class aboutus(models.Model):
    title = models.CharField(max_length=100,blank=False)
    desc = models.TextField(max_length=700,blank=False)
    image = models.ImageField(upload_to='about/',blank=False)

    def __str__(self):
        return self.title
        
class slider_us(models.Model):
    name_title = models.CharField(max_length=100,blank=False)
    descption = models.TextField(max_length=700,blank=False)
    image = models.ImageField(upload_to='slider/',blank=False)

    def __str__(self):
        return self.name_title

class our_client(models.Model):
    title_name = models.CharField(max_length=100,blank=False)
    link = models.CharField(max_length=400,blank=False)
    image = models.ImageField(upload_to='clints/',blank=False)

    def __str__(self):
        return self.title_name