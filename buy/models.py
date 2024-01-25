from django.db import models
from fruits.models import Product  # Import the Product model from your existing app
from django.contrib.auth.models import User

# Create your models here.

# Define the 'Purchase' model to represent a user's purchase of a product.
class Purchase(models.Model):
    # ForeignKey relationship with the 'User' model for the user making the purchase.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ForeignKey relationship with the 'Product' model for the purchased product.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Field to store the quantity of the purchased product.
    quantity = models.PositiveIntegerField()
    # Field to store the total price of the purchase.
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
