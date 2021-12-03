from django.urls import path
from . import views

urlpatterns = [
    #rotas login
    path('telaLogin/', views.telaLogin, name='telaLogin'),
    path('telaCadastro/', views.telaCadastro, name='telaCadastro'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('logar', views.logar, name='logar'),
    path('sair/', views.sair, name='sair'),


    #rotas chamados
    path('', views.home, name='home'),

    path('chamado/', views.home_chamado, name='home_chamado'),
    path('form_chamado/', views.form_chamado, name='form_chamado'),
    path('create_chamado/', views.create_chamado, name='create_chamado'),
    path('view_chamado/<int:pk>/', views.view_chamado, name='view_chamado'),
    path('edit_chamado/<int:pk>/', views.edit_chamado, name='edit_chamado'),
    path('update_chamado/<int:pk>/', views.update_chamado, name='update_chamado'),
    path('delete_chamado/<int:pk>/', views.delete_chamado, name='delete_chamado'),

    #rotas status
    path('status/', views.home_status, name='home_status'),
    path('form_status/', views.form_status, name='form_status'),
    path('create_status/', views.create_status, name='create_status'),
    path('view_status/<int:pk>/', views.view_status, name='view_status'),
    path('edit_status/<int:pk>/', views.edit_status, name='edit_status'),
    path('update_status/<int:pk>/', views.update_status, name='update_status'),
    path('delete_status/<int:pk>/', views.delete_status, name='delete_status'),

    #rotas categoria
    path('categoria/', views.home_categoria, name='home_categoria'),
    path('form_categoria/', views.form_categoria, name='form_categoria'),
    path('create_categoria/', views.create_categoria, name='create_categoria'),
    path('view_categoria/<int:pk>/', views.view_categoria, name='view_categoria'),
    path('edit_categoria/<int:pk>/', views.edit_categoria, name='edit_categoria'),
    path('update_categoria/<int:pk>/', views.update_categoria, name='update_categoria'),
    path('delete_categoria/<int:pk>/', views.delete_categoria, name='delete_categoria'),

    #rotas pessoa
    path('pessoa/', views.home_pessoa, name='home_pessoa'),
    path('form_pessoa/', views.form_pessoa, name='form_pessoa'),
    path('create_pessoa/', views.create_pessoa, name='create_pessoa'),
    path('view_pessoa/<int:pk>/', views.view_pessoa, name='view_pessoa'),
    path('edit_pessoa/<int:pk>/', views.edit_pessoa, name='edit_pessoa'),
    path('update_pessoa/<int:pk>/', views.update_pessoa, name='update_pessoa'),
    path('delete_pessoa/<int:pk>/', views.delete_pessoa, name='delete_pessoa'),
]
