from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, CardForm
from .models import Category, Card
import random

def index(request):
    return render(request, 'cards/index.html')

def add_card(request):
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

def categories(request):
    categories = Category.objects.all()
    return render(request, 'cards/categories.html', {'categories': categories})

def game(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    all_cards = list(Card.objects.filter(category=category))
    
    # Обработка количества карточек
    try:
        num_cards = min(len(all_cards), max(3, int(request.GET.get('num_cards', 5))))
    except:
        num_cards = min(len(all_cards), 5)
    
    if len(all_cards) >= num_cards:
        selected_cards = random.sample(all_cards, num_cards)
    else:
        selected_cards = all_cards
    
    # Генерация вариантов ответов для каждой карточки
    for card in selected_cards:
        other_cards = [c for c in all_cards if c != card]
        wrong_answers = random.sample(other_cards, min(3, len(other_cards)))
        options = wrong_answers + [card]
        random.shuffle(options)
        card.options = options
    
    if request.method == 'POST':
        correct = 0
        results = []
        
        for card in selected_cards:
            answer_id = request.POST.get(f'card_{card.id}')
            answer = next((c for c in all_cards if str(c.id) == answer_id), None)
            is_correct = (answer.right_text == card.right_text) if answer else False
            
            if is_correct:
                correct += 1
            
            results.append({
                'question': card.left_text,
                'answer': answer.right_text if answer else "Нет ответа",
                'correct_answer': card.right_text,
                'is_correct': is_correct
            })
        
        return render(request, 'cards/results.html', {
            'results': results,
            'correct': correct,
            'total': len(selected_cards),
            'percentage': int((correct / len(selected_cards)) * 100) if selected_cards else 0
        })
    
    return render(request, 'cards/game.html', {
        'category': category,
        'cards': selected_cards,
    })