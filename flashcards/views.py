from django.shortcuts import render
from .models import Category, Flashcard

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'flashcards/category_list.html', {'categories': categories})

def flashcard_list(request, category_id):
    flashcards = Flashcard.objects.filter(category_id=category_id).prefetch_related('choices')
    return render(request, 'flashcards/flashcard_list.html', {'flashcards': flashcards})

