from django.shortcuts import render

def index(request):
    '''To render the index page'''
    return render(request, 'index.html', {})
