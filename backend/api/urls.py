from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.getUsers),
    path('user/<int:pk>',views.getUser),
    path('deleteuser/<int:id>',views.DeleteUser),
    path('user/<str:username>',views.getUserByUsername),
    path('products/',views.All_Products),
    path('product/<int:id>',views.pproduct),
    path('companies/',views.Companies),
    path('<int:company>/categories',views.category),
    path('<int:company>/<int:category>/products',views.products),
    path('<int:company>/<int:category>/<int:product>',views.product),
] 