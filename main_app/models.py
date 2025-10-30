from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name


class Photo(models.Model):
    url = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True) 
    updated_at = models.DateField(auto_now=True)
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return self.url