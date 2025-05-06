from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Produto
from .forms import ProdutoForm
from django.db.models import Q
from django.urls import reverse_lazy

class ListaProdutoView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'lista_produto.html'
    context_object_name = 'produtos'
    login_url = '/login/'  # Redirecionamento para a página de login caso o usuário não esteja autenticado

    def get_queryset(self):
        queryset = super().get_queryset().order_by('codigo')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(marca__icontains=search) | 
                Q(codigo__icontains=search) |
                Q(nome__icontains=search)
                )
        return queryset

class NovoProdutoView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'novo_produto.html'
    success_url = reverse_lazy('lista_produto')
    login_url = '/login/'  # Redirecionamento para a página de login caso o usuário não esteja autenticado

class EditaProdutoView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'edita_produto.html'
    success_url = reverse_lazy('lista_produto')
    context_object_name = 'produtos'
    login_url = '/login/'  # Redirecionamento para a página de login caso o usuário não esteja autenticado
   
class RemoveProdutoView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'removido.html'
    success_url = reverse_lazy('lista_produto')
    login_url = '/login/'  # Redirecionamento para a página de login caso o usuário não esteja autenticado
