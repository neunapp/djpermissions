#
from django.urls import path

from . import views

app_name = "nota_app"

urlpatterns = [
    path(
        '', 
        views.IndexView.as_view(),
        name='index',
    ),
    path(
        'lista-notas', 
        views.NotasListView.as_view(),
        name='lista',
    ),
    path(
        'add-notas', 
        views.NotaCreateView.as_view(),
        name='add',
    ),
    path(
        'detail-notas/<pk>/', 
        views.NotaDetailView.as_view(),
        name='detail',
    ),
]