from django.contrib import admin
from .models import Company,Category,Product,Color,Size,Image

admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Image)