# views.py (полная версия)
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, CardForm
from .models import Category, Card
import random

def index(request):
    return render(request, 'cards/index.html')

def add_card(request):  # Добавьте эту функцию
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CardForm()
    return render(request, 'cards/add_card.html', {'form': form})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'cards/add_category.html', {'form': form})

def match_game(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        all_cards = list(Card.objects.filter(category=category))
        
        # Обработка количества карточек
        num_cards = int(request.GET.get('num_cards', 5))
        num_cards = min(max(num_cards, 3), min(20, len(all_cards)))
        
        selected_cards = random.sample(all_cards, num_cards)
        random.shuffle(selected_cards)
        
        if request.method == 'POST':
            correct = 0
            results = []
            
            for card in selected_cards:
                answer_id = request.POST.get(f'card_{card.id}')
                answer = next((c for c in all_cards if str(c.id) == answer_id), None)
                is_correct = answer == card
                
                if is_correct:
                    correct += 1
                
                results.append({
                    'question': card.left_text,
                    'answer': answer.right_text if answer else None,
                    'correct_answer': card.right_text,
                    'is_correct': is_correct
                })
            
            return render(request, 'cards/results.html', {
                'results': results,
                'correct': correct,
                'total': num_cards,
                'percentage': int((correct / num_cards) * 100) if num_cards > 0 else 0
            })
        
        return render(request, 'cards/game.html', {
            'category': category,
            'cards': selected_cards,
            'all_cards': all_cards,
            'num_cards': num_cards
        })
    
    categories = Category.objects.all()
    return render(request, 'cards/categories.html', {'categories': categories})