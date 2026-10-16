from django.urls import path
from . import views

app_name = 'eventos'
urlpatterns = [
    path('', views.index, name='index'),
    path("eventos/<int:pk>/", views.detalhe, name="detalhe"),
    path("locais/<int:pk>/", views.local, name="local"),
]