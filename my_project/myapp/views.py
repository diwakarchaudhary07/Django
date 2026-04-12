from django.shortcuts import render
from .models import *  ## Importing all models from the current app's models.py file

# Create your views here.
def home(request):
    return render(request, 'index.html')
def dashboard(request):
    return render(request, 'dashboard.html')

def category_products(request):
    categories = ProductCategory.objects.prefetch_related('product').all()
    return render(request, 'product.html', {'categories': categories})
