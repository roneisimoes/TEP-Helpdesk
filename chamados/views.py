from django.shortcuts import render, redirect
from chamados.forms import CategoriaForm
from chamados.models import Categoria
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    dados = {}
    #dados['db'] = Categoria.objects.all()
    all = Categoria.objects.all()
    paginator = Paginator(all,3)
    pages = request.GET.get('page')
    dados['db'] = paginator.get_page(pages)
    return render(request, 'index.html', dados)

def form(request):
    data = {}
    data['form'] = CategoriaForm()
    return render(request, 'form.html', data)

def create(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Categoria.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Categoria.objects.get(pk=pk)
    data['form'] = CategoriaForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Categoria.objects.get(pk=pk)
    form = CategoriaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Categoria.objects.get(pk=pk)
    db.delete()
    return redirect('home')