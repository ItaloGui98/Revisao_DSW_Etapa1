from django.db import models

# Create your models here.
class Local(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    endereco = models.CharField(max_length=200)
    capacidade = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descrição = models.TextField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey(Local, on_delete=models.PROTECT,related_name="eventos")
    categorias = models.ManyToManyField(Categoria, related_name="eventos", blank=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["inicio"]

    def __str__(self):
        return self.titulo

    def vagas_restantes(self):
        return self.local.capacidade - self.inscricoes.count()

class Atividade(models.Model):
    titulo = models.CharField(max_length=200)
    palestrante = models.CharField(max_length=100)
    horario = models.TimeField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="atividades")

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"
        ordering = ["horario"]

    def __str__(self):
        return self.titulo

class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    inscrito_em = models.DateTimeField(auto_now_add=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="inscricoes")

    class Meta:
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"
        ordering = ["inscrito_em"]

    def __str__(self):
        return f"{self.nome} - {self.evento.titulo}"

class Relatorio(models.Model):
    presentes = models.PositiveIntegerField()
    observaçoes = models.TextField(blank=True)
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE, related_name = "relatorio")

    class Meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"

    def __str__(self):
        return f"Relatório: {self.evento.titulo}"

