from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.usuario.username

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.usuario.username} em {self.artigo.titulo}"

class Rating(models.Model):
    artigo = models.OneToOneField(Artigo, on_delete=models.CASCADE)
    avaliacao = models.FloatField()

    def __str__(self):
        return f"Avaliação para {self.artigo.titulo}: {self.avaliacao}"
