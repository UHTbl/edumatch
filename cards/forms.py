from django import forms
from .models import Card, Category


class CardForm(forms.ModelForm):
    """Форма для создания/редактирования карточек"""
    class Meta:
        model = Card
        fields = ['left_text', 'right_text', 'category']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'left_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вопрос'
            }),
            'right_text': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Введите ответ'
            }),
        }


class CategoryForm(forms.ModelForm):
    """Форма для создания/редактирования категорий"""
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название категории'
            })
        }