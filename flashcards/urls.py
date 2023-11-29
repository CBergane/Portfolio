from django.urls import path
from . import views

app_name = 'flashcards'
urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:category_id>/flashcards/', views.flashcard_list, name='flashcard_list'),
    # Lägg till fler URL-mönster här vid behov
]
