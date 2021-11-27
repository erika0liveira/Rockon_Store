from django.shortcuts import redirect, render
from django.contrib.auth.models import User, AbstractUser
from django.contrib import auth
from .models import Usuario

def cadastro(request):
    # Teste para verificar se o método POST em cadastro.html está funcionando certo, se sim vai para a pág de login
    if request.method == 'POST':
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        Usuario.documento == request.POST['documento']
        Usuario.endereco == request.POST['endereco']
        Usuario.numero == request.POST['numero']
        Usuario.cep == request.POST['cep']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        if Usuario.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        user = Usuario.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request,'clientes/cadastro.html')


def login(request):
    # Teste para verificar se o método POST está funcionando para realizar o login
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email == "" or senha == "":
            return redirect ('login')

        print(email, senha)
        
        if Usuario.objects.filter(email=email).exists():
            nome = Usuario.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('index')
    else:
        return render(request, 'clientes/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def perfil(request):
    pass

def carrinho(request):
    if request.user.is_authenticated:
        return render(request, 'carrinho/carrinho.html')
    else:
        return redirect('index')