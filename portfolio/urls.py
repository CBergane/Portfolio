from django.urls import path
from . import views

app_name = 'bergane'

urlpatterns = [
    path('', views.index, name='index'),
 #   path('contact/', views.ContactView.as_view(), name='contact'),
 #   path('portfolio/', views.PortfolioView.as_view(), name='portfolios'),
 #   path('portfolio/<slug:slug>', views.PortfolioDetailsView.as_view(), name='portfolio'),
 #   path('blog/', views.BlogView.as_view(), name='blogs'),
 #   path('blog/<slug:slug>', views.BlogDetailsView.as_view(), name='blog'),
]