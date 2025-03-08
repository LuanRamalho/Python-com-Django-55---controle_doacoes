from django import forms
from .models import Doador, ItemDoado, Campanha, Doacao

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'email', 'telefone']

class ItemDoadoForm(forms.ModelForm):
    class Meta:
        model = ItemDoado
        fields = ['nome_item', 'quantidade', 'descricao']

class CampanhaForm(forms.ModelForm):
    data_inicio = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y'],
        label="Data de Início"
    )

    data_fim = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y'],
        label="Data de Fim"
    )

    class Meta:
        model = Campanha
        fields = ['nome_campanha', 'data_inicio', 'data_fim']



class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['doador', 'item', 'campanha', 'data_doacao']

    data_doacao = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']  # Define o formato da data, se necessário
    )
