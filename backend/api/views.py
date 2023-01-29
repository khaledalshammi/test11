from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import (UserSerializer,CompanySerializer,
ProductSerializer,CategorySerializer)
from rest_framework.response import Response
from .models import Company,Category,Product,Color,Size,Image

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request,pk):
    data = request.user
    serializer = UserSerializer(data)
    ff = User.objects.get(username=data)
    return Response(serializer.data)

@api_view(['GET'])
def getUserByUsername(request,username):
    user = User.objects.get(username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteUser(request,id):
    DeleteUser = User.objects.get(id=id)
    DeleteUser.delete()
    return Response("User has been deleted")

@api_view(['GET'])
def All_Products(request):
    pro = Product.objects.all()
    ser = ProductSerializer(pro,many=True)
    return Response(ser.data)

@api_view(['GET'])
def pproduct(request,id):
    pro = Product.objects.get(id=id)
    ser = ProductSerializer(pro)
    return Response(ser.data)

@api_view(['GET'])
def Companies(request):
    com = Company.objects.all()
    ser =CompanySerializer(com,many=True)
    return Response(ser.data)

@api_view(['GET'])
def category(request,company):
    cat = Category.objects.filter(company__id=company)
    ser =CategorySerializer(cat,many=True)
    return Response(ser.data)

@api_view(['GET'])
def products(request,company,category):
    cat = Product.objects.filter(category__id=category,
        category__company__id=company)
    ser =ProductSerializer(cat,many=True)
    return Response(ser.data)

@api_view(['GET'])
def product(request,company,category,product):
    cat = Product.objects.get(category__id=category,
        category__company__id=company,id=product)
    ser =ProductSerializer(cat)
    return Response(ser.data)