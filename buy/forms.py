from django import forms

class PurchaseForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    # Add fields for shipping information, payment details, etc.