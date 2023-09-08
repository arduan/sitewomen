from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'float': 34.53,
            'lst': [2, 4, 3, 'Hello World', True],
            'set': {3, 4, 5, 6},
            'dict': {'name': 'Vitaliy', 'age': 63},
            'value': 'Текущее время',
            }
    return render(request, 'index.html', context=data)


def about(request):
    return render(request, 'about.html', {'title': 'О сайте', })


def categories(request, cat_id):
    return HttpResponse(f"<h1>Это список категорий</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Это список категорий</h1><p>slug: {cat_slug}</p>")
