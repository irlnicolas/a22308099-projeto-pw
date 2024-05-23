from django.urls import path
from .views import view_filmes, view_filme

urlpatterns = [
    path('filmes/', view_filmes, name="filmes"),
    path('filme/<str:nome>/', view_filme, name="filme")
]