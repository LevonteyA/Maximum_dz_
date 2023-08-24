# from django import forms
#
# class AdvertisementForm(forms.Form):
#     #задаём поле для названия
#     title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
#     auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))

from django.forms import ModelForm, ValidationError
from .models import OnlineShop
from django import forms
class OnlineShopForm(ModelForm):
    class Meta:
        model = OnlineShop
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
        'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }

def clean_title(self):
    title = self.cleaned_data.get('title')
    if title.startswith('?'):
        raise ValidationError("Title cannot start with a question mark")
    return title