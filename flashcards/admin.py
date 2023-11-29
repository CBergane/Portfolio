from django.contrib import admin
from .models import Category, Flashcard, Choice

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'is_multiple_choice']
    list_filter = ['category', 'is_multiple_choice']

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'flashcard', 'is_correct']
    list_filter = ['flashcard', 'is_correct']
