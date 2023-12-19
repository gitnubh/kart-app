from django.db import models
from django.urls import reverse

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(max_length=300,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_gallery',blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return  reverse('shopping_app:products_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Products(models.Model):
    name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(max_length=300,unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_gallery',blank=True)
    stock = models.IntegerField()
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shopping_app:prodCatDetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)