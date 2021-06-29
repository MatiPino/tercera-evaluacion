from django.urls import path
from . import views

urlpatterns = [
    path('categoria/', views.categoria, name='categoria')
]