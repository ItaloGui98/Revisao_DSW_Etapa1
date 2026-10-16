from django.contrib import admin
from .models import Local, Categoria, Evento, Atividade, Inscricao, Relatorio

# Register your models here.
@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'capacidade')
    search_fields = ('nome',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class AtividadeInline(admin.TabularInline):
    model = Atividade
    extra = 1

class RelatorioInline(admin.TabularInline):
    model = Relatorio
    extra = 0

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'inicio', 'local')
    search_fields = ('titulo',)
    list_filter = ('local', 'categorias')
    inlines = [AtividadeInline, RelatorioInline]

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'palestrante', 'horario', 'evento')
    search_fields = ('titulo', 'palestrante')
    list_filter = ('evento',)

@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('evento', 'presentes')

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'evento')
    search_fields = ('nome', 'email')
    list_filter = ('evento',)






