from app.models import FornecedorIndividual
from django import forms

class InsereFornecedorForm(forms.ModelForm):

    class Meta:
        model = FornecedorIndividual

        fields = [
            'nomeprop',
            'cpf',
            'dap',
            'uf',
            'municipio',
            'bairro',
            'rua',
            'numero',
            'tel_fixo',
            'celular',
            'email',
        ]
