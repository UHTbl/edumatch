from django.contrib import admin
from .models import Category, Card  # Импортируйте ваши модели

# Регистрация модели Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Поля для отображения в списке

# Регистрация модели Card
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("left_text", "right_text", "category")  # Поля для отображения
    list_filter = ("category",)  # Фильтры справа
