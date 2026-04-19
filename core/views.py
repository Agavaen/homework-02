from django.shortcuts import render
import requests


def home_view(request):
    return render(request, 'core/home.html')


def list_view(request):
    return render(request, 'core/list_page.html')


def card_view(request):
    card = {
        'title': 'Ноутбук',
        'description': 'Мощный ноутбук для работы и учебы',
        'price': '350000 тг'
    }
    return render(request, 'core/card_page.html', {'card': card})


def api_view(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    return render(request, 'core/api_page.html', {'users': users})