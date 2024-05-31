from django import forms
from .models import item

class itemform(forms.ModelForm):
    class Meta:
        model=item
        fields=['item_name', 'item_desc', 'item_price', 'item_image']