from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    name  = forms.CharField(max_length=255)
    email =forms.EmailField()
    description = forms.CharField(max_length=255,
                                  required=False,
                                  widget=forms.Textarea(attrs={
                                      "placeholder": "A description",
                                      "class": "new-class-name two",
                                      "id": "my-id-for-textarea",
                                      "rows":20,
                                      "cols":120
                                      }))
    price = forms.DecimalField(max_digits=100, decimal_places=2, initial=50)
    
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
        ]
    
    def clean_email(self, *args, **kwargs):
        email =self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email
        
class RawProductForm(forms.Form):
    name  = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255,
                                  required=False,
                                  widget=forms.Textarea(attrs={
                                      "placeholder": "A description",
                                      "class": "new-class-name two",
                                      "id": "my-id-for-textarea",
                                      "rows":20,
                                      "cols":120
                                      }))
    price = forms.DecimalField(max_digits=100, decimal_places=2)