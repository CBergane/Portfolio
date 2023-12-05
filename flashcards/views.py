from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Flashcard

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'flashcards/category_list.html', {'categories': categories})

def flashcard_list(request, category_id):
    flashcards = Flashcard.objects.filter(category_id=category_id).prefetch_related('choices')
    paginator = Paginator(flashcards, 10)  # Visa 10 kort per sida

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'flashcards/flashcard_list.html', {'page_obj': page_obj})

