from django.contrib import admin
from .models import Category, Card


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Category"""
    list_display = ("name",)  # Отображаемое поле в списке


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Card"""
    list_display = ("left_text", "right_text", "category")  # Поля для отображения
    list_filter = ("category",)  # Фильтрация по категориям