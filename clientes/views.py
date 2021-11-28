from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser
User = get_user_model()

def cadastro(request):
    # Teste para verificar se o método POST em cadastro.html está funcionando certo, se sim vai para a pág de login
    if request.method == 'POST':
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        documento = request.POST['documento']
        endereco = request.POST['endereco']
        numero = request.POST['numero']
        cep = request.POST['cep']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
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
        else:
            user = User.objects.create_user(
                username = nome,
                first_name = nome,
                last_name = sobrenome,
                documento = documento,
                email = email,
                password = senha,
                cep = cep,
                endereco = endereco,
                numero = numero,)
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