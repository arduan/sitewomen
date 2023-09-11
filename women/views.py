from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелино Джоли', 'content': 'Биография Анджелины Джоли', 'is_public': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_public': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_public': True},

]


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'float': 34.53,
            'lst': [2, 4, 3, 'Hello World', True],
            'set': {3, 4, 5, 6},
            'dict': {'name': 'Vitaliy', 'age': 63},
            'value': 'Текущее время',
            'posts': data_db
            }
    return render(request, 'index.html', context=data)


def about(request):
    return render(request, 'about.html', {'title': 'О сайте', 'menu': menu })


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request):
    return HttpResponse("Добавить статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
