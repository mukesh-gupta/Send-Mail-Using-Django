from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=50,blank=True)
    desc=models.TextField(max_length=2000,blank=True)
    image=models.ImageField(upload_to='pcs')
    email=models.EmailField(default='example@.com')
    def __str__(self):
        return str(self.name)