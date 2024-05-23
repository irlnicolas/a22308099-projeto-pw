from django.urls import path
from .views import view_bandas, view_banda, view_album, view_musica

urlpatterns = [
    path('', view_bandas, name='bandas'),
    path('banda/<str:nome>/', view_banda, name="banda"),
    path('album/<str:titulo>/', view_album, name="album"),
    path('musica/<str:titulo>/', view_musica, name="musica")
]