from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=254)
    Number = models.CharField(max_length=12)
    Text_area = models.TextField()
    Date = models.CharField(max_length=50)
     
    def __str__(self):
         return self.Name
     