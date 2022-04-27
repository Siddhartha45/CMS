from django import forms
from .models import Product


class AddPostForm(forms.ModelForm):
    photo = forms.ImageField()
    
    class Meta:
        model = Product
        fields = ['name', 'brand', 'description', 'price', 'photo', 'size', 'clothes_type']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
                    'brand':forms.TextInput(attrs={'class':'form-control'}),
                    #'description':forms.TextInput(attrs={'class':'form-control'}),
                    #'price':forms.TextInput(attrs={'class':'form-control'}),
                    'photo':forms.FileInput(attrs={'class':'form-control'}),
                    'size':forms.Select(attrs={'class':'form-control'}),
                    'clothes_type':forms.Select(attrs={'class':'form-control'}),
                    #'contact_number':forms.TextInput(attrs={'class':'form-control'})
                  }