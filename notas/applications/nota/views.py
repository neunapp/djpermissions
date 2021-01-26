from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView
)
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseForbidden

#
from .models import Nota

class IndexView(TemplateView):
    template_name = "nota/index.html"


class NotasListView(PermissionRequiredMixin, ListView):
    model = Nota
    context_object_name = 'notas'
    template_name = "nota/lista.html"
    permission_required = 'nota.view_nota'
    permission_denied_message = 'no estas autorizado'


class NotaCreateView(CreateView):
    model = Nota
    fields = ('__all__')
    template_name = "nota/add.html"
    success_url = reverse_lazy('nota_app:lista')


class NotaDetailView(DetailView):
    model = Nota
    template_name = "nota/detail.html"

    def get(self, request, **kwargs):
        # verificamos permisos
        if not self.request.user.has_perm('nota.view_nota') :
            return HttpResponseForbidden()
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

