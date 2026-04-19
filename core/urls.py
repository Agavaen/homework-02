from django.urls import path
from .views import home_view, list_view, card_view, api_view

urlpatterns = [
    path('', home_view, name='home'),
    path('list/', list_view, name='list_page'),
    path('card/', card_view, name='card_page'),
    path('api/', api_view, name='api_page'),
]