from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CadastroUsuarioForm

# tela de login
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tela_inicial')
        else:
            return render(request, 'index.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'index.html')

# redirect do login
@login_required
def tela_inicial(request):
    return render(request, 'tela_inicial.html')

# cadastarar usuario

def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redireciona para login após cadastro
    else:
        form = CadastroUsuarioForm()
    return render(request, 'cadastro.html', {'form': form})