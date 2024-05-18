from django import forms

from .models import Item

INPUT_ATTR = "w-full py-4 px-6 rounded-xl border bg-gray-100 bg-opacity-50"

class NewItemForm(forms.ModelForm):

    currency_choices = [
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('INR', '₹'),
        ('MAD', 'د.م'),
    ]

    currency = forms.ChoiceField(choices=currency_choices, initial='USD', widget=forms.Select(attrs={'class': INPUT_ATTR}))

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price','currency', 'image', )
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_ATTR
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_ATTR
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_ATTR
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_ATTR
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_ATTR
            })
        }


class EditItemForm(forms.ModelForm):

    currency_choices = [
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        ('INR', '₹'),
        ('MAD', 'د.م'),
    ]

    currency = forms.ChoiceField(choices=currency_choices, initial='USD', widget=forms.Select(attrs={'class': INPUT_ATTR}))

    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'currency','image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_ATTR
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_ATTR
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_ATTR
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_ATTR
            })
        }