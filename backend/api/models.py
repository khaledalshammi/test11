from django.db import models
from .gen import get_code
from django.db.models.signals import post_save

class Company(models.Model):
    name         = models.CharField(max_length=150,unique=True)
    description  = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Category(models.Model):
    name    = models.CharField(max_length=150)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.name +"("+self.company.name+')'

class Product(models.Model):
    name          = models.CharField(max_length=150,unique=True)
    price         = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(upload_to='photos/product')
    description   = models.CharField(max_length=500)
    has_size      = models.BooleanField(default=True)
    has_color     = models.BooleanField(default=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    is_available  = models.BooleanField(default=True)
    code          = models.CharField(max_length=50,null=True,blank=True)
    category      = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Color(models.Model):
    color    = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    product  = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.color

class Size(models.Model):
    size     = models.CharField(max_length=5,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    product  = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.size

class Image(models.Model):
    images = models.ImageField(upload_to='photos/products',null=True,blank=True)
    product  = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.product.name

def post_save_Product_Code(sender, instance, created, *args, **kwargs):
    if created:
        product = instance.name
        two_first = product[0:2]
        two_last = product[len(product)-2:len(product)]
        our_code = get_code()
        our_code += str(two_first)
        our_code += str(two_last)
        instance.code = our_code
        instance.save()

post_save.connect(post_save_Product_Code, sender=Product)