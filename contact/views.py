from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# Define a view for handling the contact form submission.
def contact(request):
    if request.method == 'POST':
        # Create an instance of the ContactForm with data from the POST request.
        form = ContactForm(request.POST)
        
        # Check if the form data is valid.
        if form.is_valid(): 
            # Save the form data to the Contact model.
            form.save()
            
            # Compose an email subject and message.
            subject = "Welcome to PythonGuides Training Course"
            message = "Our team will contact you within 24hrs."
            
            # Get the sender's email address from Django settings.
            email_from = settings.EMAIL_HOST_USER
            
            # Get the recipient's email from the cleaned form data.
            email = form.cleaned_data['email']
            
            # Create a recipient list with the recipient's email address.
            recipient_list = email
            
            # Send an email using Django's send_mail function.
            send_mail(subject, message, email_from, [recipient_list])
            
            # Render a success page after a successful form submission.
            return render(request, 'success.html') 
    else:
        # If the request method is not POST, create an empty ContactForm instance.
        form = ContactForm()
    
    # Define a context containing the form to be passed to the 'contact.html' template.
    context = {'form': form}
    
    # Render the 'contact.html' template with the form and context.
    return render(request, 'contact.html', context)
