from django.shortcuts import render, redirect, get_object_or_404
from .models import Doador, ItemDoado, Campanha, Doacao
from .forms import DoadorForm, ItemDoadoForm, CampanhaForm, DoacaoForm
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# --- Listar doadores ---
def listar_doadores(request):
    doadores = Doador.objects.all()
    return render(request, 'doacoes/listar_doadores.html', {'doadores': doadores})

# --- Cadastrar doador ---
def cadastrar_doador(request):
    if request.method == 'POST':
        form = DoadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_doadores')
    else:
        form = DoadorForm()
    return render(request, 'doacoes/cadastrar_doador.html', {'form': form})

# --- Editar doador ---
def editar_doador(request, pk):
    doador = get_object_or_404(Doador, pk=pk)
    if request.method == 'POST':
        form = DoadorForm(request.POST, instance=doador)
        if form.is_valid():
            form.save()
            return redirect('listar_doadores')
    else:
        form = DoadorForm(instance=doador)
    return render(request, 'doacoes/cadastrar_doador.html', {'form': form})

# --- Excluir doador ---
def excluir_doador(request, pk):
    doador = get_object_or_404(Doador, pk=pk)
    doador.delete()
    return redirect('listar_doadores')

# --- Listar itens doados ---
def listar_itens(request):
    itens = ItemDoado.objects.all()
    return render(request, 'doacoes/listar_itens.html', {'itens': itens})

# --- Cadastrar item doado ---
def cadastrar_item(request):
    if request.method == 'POST':
        form = ItemDoadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_itens')
    else:
        form = ItemDoadoForm()
    return render(request, 'doacoes/cadastrar_item.html', {'form': form})

# --- Editar item doado ---
def editar_item(request, pk):
    item = get_object_or_404(ItemDoado, pk=pk)
    if request.method == 'POST':
        form = ItemDoadoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('listar_itens')
    else:
        form = ItemDoadoForm(instance=item)
    return render(request, 'doacoes/cadastrar_item.html', {'form': form})

# --- Excluir item doado ---
def excluir_item(request, pk):
    item = get_object_or_404(ItemDoado, pk=pk)
    item.delete()
    return redirect('listar_itens')

# --- Listar campanhas ---
def listar_campanhas(request):
    campanhas = Campanha.objects.all()
    return render(request, 'doacoes/listar_campanhas.html', {'campanhas': campanhas})

# --- Cadastrar campanha ---
def cadastrar_campanha(request):
    if request.method == "POST":
        form = CampanhaForm(request.POST)
        if form.is_valid():
            campanha = form.save()  # Salva a campanha sem os doadores
            return redirect('listar_campanhas')  # Redireciona para a página de listagem de campanhas
    else:
        form = CampanhaForm()

    return render(request, 'doacoes/cadastrar_campanha.html', {'form': form})

# --- Editar campanha ---
def editar_campanha(request, pk):
    campanha = get_object_or_404(Campanha, pk=pk)
    if request.method == 'POST':
        form = CampanhaForm(request.POST, instance=campanha)
        if form.is_valid():
            form.save()
            return redirect('listar_campanhas')
    else:
        form = CampanhaForm(instance=campanha)
    return render(request, 'doacoes/cadastrar_campanha.html', {'form': form})

# --- Excluir campanha ---
def excluir_campanha(request, pk):
    campanha = get_object_or_404(Campanha, pk=pk)
    campanha.delete()
    return redirect('listar_campanhas')

# --- Listar doações ---
def listar_doacoes(request):
    doacoes = Doacao.objects.all()
    return render(request, 'doacoes/listar_doacoes.html', {'doacoes': doacoes})

# --- Cadastrar doação ---
def cadastrar_doacao(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_doacoes')
    else:
        form = DoacaoForm()
    return render(request, 'doacoes/cadastrar_doacao.html', {'form': form})

# --- Editar doação ---
def editar_doacao(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)
    if request.method == 'POST':
        form = DoacaoForm(request.POST, instance=doacao)
        if form.is_valid():
            form.save()
            return redirect('listar_doacoes')
    else:
        form = DoacaoForm(instance=doacao)
    return render(request, 'doacoes/cadastrar_doacao.html', {'form': form})

# --- Excluir doação ---
def excluir_doacao(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)
    doacao.delete()
    return redirect('listar_doacoes')

# --- Gerar relatório de doações ---
def gerar_relatorio(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_doacoes.pdf"'

    c = canvas.Canvas(response, pagesize=letter)
    c.drawString(100, 750, "Relatório de Doações")

    doacoes = Doacao.objects.all()
    y_position = 730
    for doacao in doacoes:
        data_formatada = doacao.data_doacao.strftime('%d/%m/%Y')
        c.drawString(100, y_position, f'Doador: {doacao.doador.nome} | Item: {doacao.item.nome_item} | Data: {data_formatada}')
        y_position -= 20

    c.showPage()
    c.save()
    return response
