from django.db import models

# Category Model
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    category_description = models.TextField(blank=True, null=True)
    manufacture_date = models.DateField()  
    expire_date = models.DateField()        
    def __str__(self):
        return self.category_name


# Product Model
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products/')

    # ForeignKey to  Category added.
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="products",
        default=1
    )

    def __str__(self):
        return self.product_name
