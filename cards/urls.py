from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_card, name='add_card'),
    path('add-category/', views.add_category, name='add_category'),
    path('categories/', views.categories, name='categories'),
    path('game/<int:category_id>/', views.game, name='game'),
]