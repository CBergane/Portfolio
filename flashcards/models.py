from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    category = models.ForeignKey(Category, related_name='flashcards', on_delete=models.CASCADE)
    question = RichTextField()
    answer = RichTextField()
    is_multiple_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class Choice(models.Model):
    flashcard = models.ForeignKey(Flashcard, related_name='choices', on_delete=models.CASCADE)
    text = RichTextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.flashcard.question[:50]} - {self.text}"


