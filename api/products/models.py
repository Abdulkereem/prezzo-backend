from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    banner_image = models.ImageField(upload_to='category_banners/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
