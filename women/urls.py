
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cat/<int:cat_id>/', views.categories),
    path('cat/<slug:cat_slug>/', views.categories_by_slug),
]