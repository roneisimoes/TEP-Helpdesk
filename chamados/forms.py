from django.forms import ModelForm
from chamados.models import Categoria, Status, Pessoa, Chamado

# Create the form class.
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['nome', 'descricao']

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'senha']

class ChamadoForm(ModelForm):
    class Meta:
        model = Chamado
        fields = ['titulo', 'descricao', 'categoria', 'status', 'responsavel']