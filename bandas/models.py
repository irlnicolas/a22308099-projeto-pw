from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='app/fotos', null=True, blank=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name="albuns")
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    capa = models.ImageField(upload_to='app/capas', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="musicas")
    titulo = models.CharField(max_length=100)
    duracao = models.DurationField()
    link = models.CharField(max_length=100, default = None)

    def __str__(self):
        return self.titulo
