from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #temporario, removerS
    path('t1', views.teste, name='teste'),
    path('t2', views.teste2, name='teste2'),
]