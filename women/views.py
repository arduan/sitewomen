from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def categories(request, cat_id):
    return HttpResponse(f"<h1>Это список категорий</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Это список категорий</h1><p>slug: {cat_slug}</p>")
