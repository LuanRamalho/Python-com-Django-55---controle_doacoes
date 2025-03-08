from django.urls import path
from . import views

urlpatterns = [
    # Doadores
    path('doadores/', views.listar_doadores, name='listar_doadores'),
    path('cadastrar_doador/', views.cadastrar_doador, name='cadastrar_doador'),
    path('editar_doador/<int:pk>/', views.editar_doador, name='editar_doador'),
    path('excluir_doador/<int:pk>/', views.excluir_doador, name='excluir_doador'),
    
    # Itens Doados
    path('itens/', views.listar_itens, name='listar_itens'),
    path('cadastrar_item/', views.cadastrar_item, name='cadastrar_item'),
    path('editar_item/<int:pk>/', views.editar_item, name='editar_item'),
    path('excluir_item/<int:pk>/', views.excluir_item, name='excluir_item'),
    
    # Campanhas
    path('campanhas/', views.listar_campanhas, name='listar_campanhas'),
    path('cadastrar_campanha/', views.cadastrar_campanha, name='cadastrar_campanha'),
    path('editar_campanha/<int:pk>/', views.editar_campanha, name='editar_campanha'),
    path('excluir_campanha/<int:pk>/', views.excluir_campanha, name='excluir_campanha'),
    
    # Doações
    path('doacoes/', views.listar_doacoes, name='listar_doacoes'),
    path('cadastrar_doacao/', views.cadastrar_doacao, name='cadastrar_doacao'),
    path('editar_doacao/<int:pk>/', views.editar_doacao, name='editar_doacao'),
    path('excluir_doacao/<int:pk>/', views.excluir_doacao, name='excluir_doacao'),
    
    # Relatório de Doações em PDF
    path('gerar_relatorio/', views.gerar_relatorio, name='gerar_relatorio'),
]
