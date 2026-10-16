from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from .models import Evento, Local, Categoria, Relatorio


def index(request):
    eventos = Evento.objects.filter(
        inicio__gte=timezone.now()
    ).select_related("local").prefetch_related("categorias")

    categoria_id = request.GET.get("categoria")

    if categoria_id and categoria_id.isdigit():
        eventos = eventos.filter(
            categorias__id=categoria_id
        )

    categorias = Categoria.objects.all()

    return render(request, "eventos/index.html", {
        "eventos": eventos,
        "categorias": categorias,
        "categoria_selecionada": categoria_id,
    })


def detalhe(request, pk):
    evento = get_object_or_404(
        Evento.objects.select_related("local"),
        pk=pk
    )

    relatorio = None

    try:
        relatorio = evento.relatorio
    except Relatorio.DoesNotExist:
        pass

    return render(request, "eventos/detalhe.html", {
        "evento": evento,
        "relatorio": relatorio,
    })


def local(request, pk):
    local = get_object_or_404(Local, pk=pk)

    eventos = local.eventos.filter(
        inicio__gte=timezone.now()
    )

    return render(request, "eventos/local.html", {
        "local": local,
        "eventos": eventos,
    })

