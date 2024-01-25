from django.db import models
from django.utils import timezone

# Create your models here.

# Define the 'Post' model, which represents posts on your website.
class Post(models.Model):
    # Auto-incrementing primary key for the Post model.
    id = models.AutoField(primary_key=True)
    # Field for the contact associated with the post, limited to 140 characters.
    contact = models.CharField(max_length=140)
    # Field for the body or content of the post, which can be a longer text.
    body = models.TextField()

    def __str__(self):
        # This method defines how the object is represented as a string (e.g., in admin).
        return self.contact

# Define the 'Contact' model, which represents contact form submissions.
class Contact(models.Model):
    # Field for the name of the person submitting the contact form, limited to 250 characters.
    name = models.CharField(max_length=250)
    # Field for the email address of the person submitting the contact form.
    email = models.EmailField()
    # Field for the phone number of the person, limited to 10 characters.
    phone = models.CharField(max_length=10)
    # Field for the mode of contact (e.g., 'email' or 'phone'), limited to 50 characters.
    mode_of_contact = models.CharField('Contact by', max_length=50)
    # Field for categories of questions or reasons for contact, limited to 50 characters.
    question_categories = models.CharField('How can we help you?', max_length=50)
    # Field for the message or content of the contact form submission, up to 3000 characters.
    message = models.TextField(max_length=3000)

    def __str__(self):
        # This method defines how the object is represented as a string (e.g., in admin).
        return self.email

# Define the 'Item' model, representing items for sale.
class Item(models.Model):
    # Field for the name of the item, limited to 100 characters.
    name = models.CharField(max_length=100)
    # Field for the price of the item, using a decimal with 10 digits and 2 decimal places.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Field for the description of the item, which can be a longer text.
    description = models.TextField()

# Define the 'Order' model, representing orders made by users.
class Order(models.Model):
    # Field for the user's name who placed the order, limited to 100 characters.
    user_name = models.CharField(max_length=100)
    # Field for the user's email address, used for order communication.
    user_email = models.EmailField()
    # Field for the shipping address of the order, which can be a longer text.
    shipping_address = models.TextField()
    # Field for the item associated with the order, creating a ForeignKey relationship with 'Item'.
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
