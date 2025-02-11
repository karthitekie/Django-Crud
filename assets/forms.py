from django import forms
from .models import *

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_name', 'serial_number', 'location', 'status', 'purchase_date']


# assets/forms.py
class MasterCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['code', 'description']  # Use lowercase for field names

