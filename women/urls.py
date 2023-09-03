
from django.urls import path
from .views import index, categories, categories_by_slug

urlpatterns = [
    path('', index),
    path('cat/<int:cat_id>/', categories),
    path('cat/<slug:cat_slug>/', categories_by_slug),
]