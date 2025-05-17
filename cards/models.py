from django.db import models


class Category(models.Model):
    """Модель категории для группировки карточек"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Card(models.Model):
    """Модель карточки с вопросом и ответом"""
    left_text = models.CharField(max_length=200)  # Текст вопроса
    right_text = models.CharField(max_length=200)  # Текст ответа
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  # Удаление карточек при удалении категории
        related_name='cards'
    )

    def __str__(self):
        return f"{self.left_text} — {self.right_text}"