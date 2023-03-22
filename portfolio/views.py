from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from .forms import ContacForm
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate
)

class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['blogs'] = blogs
        context['portfolio'] = portfolio

        return context
