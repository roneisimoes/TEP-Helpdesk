from django.shortcuts import render, redirect
from chamados.forms import CategoriaForm
from chamados.models import Categoria

# Create your views here.
def home(request):
    dados = {}
    dados['db'] = Categoria.objects.all()
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
    return render(request, 'index.html')
