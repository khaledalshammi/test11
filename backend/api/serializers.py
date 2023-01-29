from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company,Category,Product,Color,Size,Image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"    

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
    def get_company(self,obj):
        company_data = Company.objects.get(category__id=obj.id)
        ser = CompanySerializer(company_data)
        return ser.data


class ProductSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField(read_only=True)
    size = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    category = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
    
    def get_color(self,obj):
        color_data = Color.objects.filter(product=obj)
        ser = ColorSerializer(color_data,many=True)
        return ser.data
    
    def get_size(self,obj):
        size_data = Size.objects.filter(product=obj)
        ser = SizeSerializer(size_data,many=True)
        return ser.data
    
    def get_image(self,obj):
        image_data = Image.objects.filter(product=obj)
        ser = ImageSerializer(image_data,many=True)
        return ser.data

    def get_category(self,obj):
        category_data = Category.objects.get(product=obj)
        ser = CategorySerializer(category_data)
        return ser.data