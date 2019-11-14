from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    def __str__(self):
        return f"{self.name}-{self.website}"

class ShoeType(models.Model):
    style = models.CharField(max_length = 50)
    def __str__(self):
        return f"{self.style}"

class ShoeColor(models.Model):
    COLOR_CHOICES = [
        ('V', 'Violet'),
        ('I', 'Indigo'),
        ('B', 'Blue'),
        ('G', 'Green'),
        ('Y','Yellow'),
        ('O','Orange'),
        ('R','Red'),
        ('white','White'),
        ('black','Black'),
    ]
    color_name = models.CharField(max_length=5,choices=COLOR_CHOICES,default='black')
    def __str__(self):
        return f"{self.color_name}"

class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor,on_delete=models.CASCADE)
    material = models.CharField(max_length=30)
    shoe_type = models.ForeignKey(ShoeType,on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.shoe_type}-{self.manufacturer}"
