from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('custom-search/', views.custom_search, name='custom_search'),
    path('website-text/', views.get_website_text, name='website_text'),
    path('website-markdown/', views.get_website_markdown, name='website_markdown'),
]