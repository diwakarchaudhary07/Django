# ✅ Day  6 – Category , Product And HTML Tamplate 

# APP Folder => models.py

# from django.db import models

# # Category Model
# class Category(models.Model):
#     category_name = models.CharField(max_length=255)
#     category_image = models.ImageField(upload_to='categories/', null=True, blank=True)

#     def __str__(self):
#         return self.category_name


# # Product Model
# class Product(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
#     product_name = models.CharField(max_length=255)
#     product_price = models.DecimalField(max_digits=10, decimal_places=2)
#     product_description = models.TextField()
#     product_image = models.ImageField(upload_to='products/')

#     def __str__(self):
#         return self.product_name


# Step 1 :- Running Two Command 
#                python manage.py makemigrations
#                python manage.py migrate

# APP Folder => views.py

# from django.shortcuts import render
# from .models import *  ## Importing all models from the current app's models.py file

# def category_products(request):
#     categories = Category.objects.prefetch_related('products').all()
#     return render(request, 'category_products.html', {'categories': categories})

# APP Folder =>admin.py

# from django.contrib import admin
# from .models import Product, Category

# admin.site.register(Product)
# admin.site.register(Category)

# APP Folder => urls.py

# from django.contrib import admin
# from django.urls import path
# from .views import * ## Importing all views from the current app's views.py file

# urlpatterns = [
#     path('categorie', category_products, name='category_products'),
# ]

# Step 2 :- Make templates Folder Outside The APP Folder And Project Folder

# Step 3 :- Make A HTML File in (templates) File Name - category_products.html


# Templates folder => category_products.html
 
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Products by Category</title>

#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             background: #f5f5f5;
#             margin: 0;
#             padding: 20px;
#         }

#         h1 {
#             text-align: center;
#         }

#         .category {
#             margin-bottom: 50px;
#         }

#         .category-header {
#             display: flex;
#             align-items: center;
#             gap: 15px;
#             margin-bottom: 20px;
#         }

#         .category-header img {
#             width: 60px;
#             height: 60px;
#             object-fit: cover;
#             border-radius: 50%;
#         }

#         .products {
#             display: grid;
#             grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
#             gap: 20px;
#         }

#         .product-card {
#             background: white;
#             padding: 15px;
#             border-radius: 10px;
#             box-shadow: 0 2px 5px rgba(0,0,0,0.1);
#             transition: 0.3s;
#         }

#         .product-card:hover {
#             transform: translateY(-5px);
#         }

#         .product-card img {
#             width: 100%;
#             height: 150px;
#             object-fit: cover;
#             border-radius: 8px;
#         }

#         .product-name {
#             font-size: 18px;
#             font-weight: bold;
#             margin: 10px 0;
#         }

#         .price {
#             color: green;
#             font-weight: bold;
#         }

#         .description {
#             font-size: 14px;
#             color: #555;
#         }
#     </style>
# </head>
# <body>

# <h1>Products by Category</h1>

# {% for category in categories %}
# <div class="category">

#     <div class="category-header">
#         {% if category.category_image %}
#             <img src="{{ category.category_image.url }}" alt="{{ category.category_name }}">
#         {% endif %}
#         <h2>{{ category.category_name }}</h2>
#     </div>

#     <div class="products">
#         {% for product in category.products.all %}
#         <div class="product-card">
#             <img src="{{ product.product_image.url }}" alt="{{ product.product_name }}">
            
#             <div class="product-name">{{ product.product_name }}</div>
            
#             <div class="price">₹{{ product.product_price }}</div>
            
#             <div class="description">
#                 {{ product.product_description|truncatewords:10 }}
#             </div>
#         </div>
#         {% empty %}
#         <p>No products available in this category.</p>
#         {% endfor %}
#     </div>

# </div>
# {% endfor %}

# </body>
# </html>
# Run the Server Now This is The Link :-  http://127.0.0.1:8000/categorie

