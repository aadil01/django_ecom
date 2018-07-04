from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100) #slug=fetch--many record & id=fetch-single record

    def __str__(self):
        return self.name

class Products(models.Model):
    category=models.ForeignKey(Categories)
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,null=True)
    description=models.TextField(blank=True)
    pic=models.FileField(upload_to='pic',null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
