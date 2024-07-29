from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detect/', views.detect_plagiarism, name='detect_plagiarism'),
]
