from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('get_sentiment/', views.get_sentiment, name='get_sent'),
    path('get_reviews/', views.get_reviews, name='get_rev'),

]
