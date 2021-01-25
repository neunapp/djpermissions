from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView
)

#
from .models import Nota

class IndexView(TemplateView):
    template_name = "nota/index.html"


class NotasListView(ListView):
    model = Nota
    context_object_name = 'notas'
    template_name = "nota/lista.html"


class NotaCreateView(CreateView):
    model = Nota
    fields = ('__all__')
    template_name = "nota/add.html"
    success_url = reverse_lazy('nota_app:lista')


class NotaDetailView(DetailView):
    model = Nota
    template_name = "nota/detail.html"

