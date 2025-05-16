# cards/forms.py
from django import forms
from .models import Card, Category

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['left_text', 'right_text', 'category']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'left_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вопрос'}),
            'right_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ответ'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название категории'
            })
        }