from django import forms
from .models import Contact

# Define choices for the 'mode_of_contact' field.
select_mode_of_contact = (
    ("email", "E-Mail"),
    ("phone", "Phone"),
)

# Define choices for the 'question_categories' field.
select_question_categories = (
    ("certification", "Certification"),
    ("interview", "Interview"),
    ("material", "Material"),
    ("access_duration", "Access and Duration"),
    ("other", "Others"),
)

# Create a form to handle contact submissions based on the Contact model.
class ContactForm(forms.ModelForm):
    # Additional field for 'phone', not required, allowing optional phone number input.
    phone = forms.CharField(required=False)
    
    # Field for 'mode_of_contact' with radio button selection using predefined choices.
    mode_of_contact = forms.CharField(required=False, widget=forms.RadioSelect(choices=select_mode_of_contact))
    
    # Field for 'question_categories' with dropdown selection using predefined choices.
    question_categories = forms.CharField(required=False, widget=forms.Select(choices=select_question_categories))

    class Meta:
        # Associate the form with the 'Contact' model to generate form fields automatically.
        model = Contact
        # Include all fields from the 'Contact' model in the form.
        fields = '__all__'
