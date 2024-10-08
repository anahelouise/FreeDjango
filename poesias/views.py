from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def my_view(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Página</title>
</head>
<body>
    <h1>Bem-Vindo a minha pagina Django</h1>
    <p>Esta é uma pagina simples servida através de Django</p>
</body>
</html>
""")

def home(request):
    return render(request, 'home.html')

def user_view(request, username):
    return HttpResponse(f"Perfil do usuario: {username}")

def root_view(request):
    return HttpResponse("Estamos na Raiz 2. Porta 8000")

def contexto(request):
    context = {
        'nome': 'João',
        'idade': 30,
        'hobbies': ['Leitura', 'Ciclismo', 'Cozinhar']
    }
    return render(request, 'contexto.html', context)

def sobre(request):
    return render(request, 'sobre.html')

def produtos(request):
    context = {
        'nome': 'Ana Helouise',
        'autor': 'José Regi',
        'loja': 'Nossa Loja',
        'livros_disponiveis': ['Silencio Acentuado', 'Humanuscrito', 'Minha Pena']
    }
    return render(request, 'produtos.html', context)

def contato(request):
    return render(request, 'contato.html')

def perfil(request):
    return render(request, 'anahelouise.html')