from django.urls import path
from .views import * ## Importing all views from the current app's views.py file

urlpatterns = [
    path('categorie',ProductCategory, name='product'),
]
