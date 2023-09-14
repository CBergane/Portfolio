from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate
)

class IndexView(generic.TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		return context


class ContactView(generic.FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        # Save the form data to the database (assuming the ContactForm model has a save() method)
        #form.save()

        # Extract data from the form
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Prepare email content
        subject = f"New message from {name}"
        message_content = f"From: {name} <{email}>\n\n{message}"

        # Send email to yourself
        send_mail(
            subject,
            message_content,
            settings.EMAIL_HOST_USER,
            ['christian.bergane@gmail.com'],
            fail_silently=False,
        )

        messages.success(self.request, 'Tack, jag återkommer till er så snart som möjligt.')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailsView(generic.DetailView):
    model = Portfolio
    template_name = 'portfolio-detail.html'


class BlogView(generic.ListView):
    model = Blog
    template_name = 'blog.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailsView(generic.DetailView):
    model = Blog
    template_name = 'blog-detail.html'
