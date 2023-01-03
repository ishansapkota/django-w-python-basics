from django import forms

from .models import Parts

class PartsForm(forms.ModelForm):
    class Meta:
        model = Parts
        fields = {
            "parts_name",
            "parts_brand",
            "parts_manufactured_date"
        }
    # def clean(self, *args, **kwargs):
    #     cleaned_data = super(PartsForm, self).clean(*args, **kwargs)
    #     if cleaned_data['quantity'] > 10:
    #         raise forms.ValidationError('Quantity must be less than 10')
    #     return cleaned_data