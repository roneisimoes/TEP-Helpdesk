from django.shortcuts import render, redirect
from chamados.forms import CategoriaForm, ChamadoForm, StatusForm, PessoaForm
from chamados.models import Categoria, Chamado, Status, Pessoa
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'base.html')

# Categoria
def home_categoria(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Categoria.objects.filter(nome__icontains=search)
    else:
        dados['db'] = Categoria.objects.all()

    #paginator
    #all = Categoria.objects.all()
    #paginator = Paginator(all,3)
    #pages = request.GET.get('page')
    #dados['db'] = paginator.get_page(pages)
    return render(request, 'categoria.html', dados)

def form_categoria(request):
    data = {}
    data['form_categoria'] = CategoriaForm()
    return render(request, 'form_categoria.html', data)

def create_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_categoria')

def view_categoria(request, pk):
    data = {}
    data['db'] = Categoria.objects.get(pk=pk)
    return render(request, 'view_categoria.html', data)

def edit_categoria(request, pk):
    data = {}
    data['db'] = Categoria.objects.get(pk=pk)
    data['form_categoria'] = CategoriaForm(instance=data['db'])
    return render(request, 'form_categoria.html', data)

def update_categoria(request, pk):
    data = {}
    data['db'] = Categoria.objects.get(pk=pk)
    form = CategoriaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home_categoria')

def delete_categoria(request, pk):
    db = Categoria.objects.get(pk=pk)
    db.delete()
    return redirect('home_categoria')

#=====================================
#Status
#=====================================
def home_status(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Status.objects.filter(nome__icontains=search)
    else:
        dados['db'] = Status.objects.all()

    #paginator
    #all = Categoria.objects.all()
    #paginator = Paginator(all,3)
    #pages = request.GET.get('page')
    #dados['db'] = paginator.get_page(pages)
    return render(request, 'status.html', dados)

def form_status(request):
    data = {}
    data['form_status'] = StatusForm()
    return render(request, 'form_status.html', data)

def create_status(request):
    form = StatusForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_status')

def view_status(request, pk):
    data = {}
    data['db'] = Status.objects.get(pk=pk)
    return render(request, 'view_status.html', data)

def edit_status(request, pk):
    data = {}
    data['db'] = Status.objects.get(pk=pk)
    data['form_status'] = StatusForm(instance=data['db'])
    return render(request, 'form_status.html', data)

def update_status(request, pk):
    data = {}
    data['db'] = Status.objects.get(pk=pk)
    form = StatusForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home_status')

def delete_status(request, pk):
    db = Status.objects.get(pk=pk)
    db.delete()
    return redirect('home_status')

#======================================
#Pessoa
#======================================
def home_pessoa(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Pessoa.objects.filter(nome__icontains=search)
    else:
        dados['db'] = Pessoa.objects.all()

    #paginator
    #all = Categoria.objects.all()
    #paginator = Paginator(all,3)
    #pages = request.GET.get('page')
    #dados['db'] = paginator.get_page(pages)
    return render(request, 'pessoa.html', dados)

def form_pessoa(request):
    data = {}
    data['form_pessoa'] = PessoaForm()
    return render(request, 'form_pessoa.html', data)

def create_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_pessoa')

def view_pessoa(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    return render(request, 'view_pessoa.html', data)

def edit_pessoa(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    data['form_pessoa'] = PessoaForm(instance=data['db'])
    return render(request, 'form_pessoa.html', data)

def update_pessoa(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home_pessoa')

def delete_pessoa(request, pk):
    db = Pessoa.objects.get(pk=pk)
    db.delete()
    return redirect('home_pessoa')

#======================================
#Chamados
#======================================
def home_chamado(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Chamado.objects.filter(titulo__icontains=search)
    else:
        dados['db'] = Chamado.objects.all()

    #paginator
    #all = Categoria.objects.all()
    #paginator = Paginator(all,3)
    #pages = request.GET.get('page')
    #dados['db'] = paginator.get_page(pages)
    return render(request, 'chamado.html', dados)

def form_chamado(request):
    data = {}
    data['form_chamado'] = ChamadoForm()
    return render(request, 'form_chamado.html', data)

def create_chamado(request):
    form = ChamadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_chamado')

def view_chamado(request, pk):
    data = {}
    data['db'] = Chamado.objects.get(pk=pk)
    return render(request, 'view_chamado.html', data)

def edit_chamado(request, pk):
    data = {}
    data['db'] = Chamado.objects.get(pk=pk)
    data['form_chamado'] = ChamadoForm(instance=data['db'])
    return render(request, 'form_chamado.html', data)

def update_chamado(request, pk):
    data = {}
    data['db'] = Chamado.objects.get(pk=pk)
    form = ChamadoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home_chamado')

def delete_chamado(request, pk):
    db = Chamado.objects.get(pk=pk)
    db.delete()
    return redirect('home_chamado')
