from django.shortcuts import render
from chamados.forms import CategoriaForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = CategoriaForm()
    return render(request, 'form.html', data)
