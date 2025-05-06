from django.urls import path
from .views import ListaProdutoView, RemoveProdutoView, NovoProdutoView, EditaProdutoView


urlpatterns = [
    path('lista/', ListaProdutoView.as_view(), name='lista_produto'),
    path('nova/', NovoProdutoView.as_view(), name='novo_produto'),
    path('edita/<int:pk>/', EditaProdutoView.as_view(), name='edita_produto'),
    path('remove/<int:pk>/', RemoveProdutoView.as_view(), name='remove_produto'),
]