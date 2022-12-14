from django.shortcuts import render
from .models import categ, product, client
import random


# Create your views here.
def home(request):
    return render(request, 'home.html')
def registerpro(request):
    categorias = categ.objects.all()
    return render(request, 'registerpro.html', {'categ': categorias})
def cadprod(request):
    nome = request.POST.get('nome')
    quant = request.POST.get('quant')
    price = request.POST.get('price')
    sel = request.POST.get('sel')
    product.objects.create(nome=nome, quant=quant, price=price, categ=sel)
    return render(request, 'mensagem.html', {'mensagem': 'cadastro de produto efetuado com sucesso!', 'cod': 1})

def listprod(request):
    prod = product.objects.all()
    return render(request, 'listprod.html', {'prod': prod})

def editprod(request, id):
    prod = product.objects.get(id=id)
    categorias = categ.objects.all()
    return render(request, 'editprod.html', {'prod': prod, 'categ': categorias})
def confirmeditprod(request, id):
    prod = product.objects.get(id=id)
    prod.nome = request.POST.get('nome')
    prod.quant = request.POST.get('quant')
    prod.price = request.POST.get('price')
    prod.categ = request.POST.get('sel')
    prod.save()
    return render(request, 'mensagem.html', {'mensagem': 'Atualização de produto efetuada com sucesso!', 'cod': 1})


def deleteprod(request, id):
    prod = product.objects.get(id=id)
    contaa = random.randrange(1, 100)
    contab = random.randrange(1, 100)
    return render(request, 'deleteprod.html', context={'prod':prod, 'contaa':contaa, 'contab':contab})


def confirmdeleteprod(request, id):
    contaa = int(request.POST.get('contaa'))
    contab = int(request.POST.get('contab'))
    calc = int(request.POST.get('calc'))
    conta = int(contaa+contab)
    if conta == calc:
        prod = product.objects.get(id=id)
        prod.delete()
        return render(request, 'mensagem.html', {'mensagem': 'produto deletado com sucesso', 'cod': 1, 'sit': 'prod'})
    else:
        return render(request, 'mensagem.html', {'mensagem': 'Resposta do cálculo incorreta.', 'cod': 0, 'sit':'prod'}) 

def registercli(request):
    return render(request, 'registercli.html')
def cadcli(request):
    nome = request.POST.get('nome')
    email= request.POST.get('email')
    cpf = request.POST.get('cpf')
    nasc = request.POST.get('nasc')
    data = nasc.split('-')
    nasc = data[2]+'/' + data[1]+'/' +data[0]
    card = request.POST.get('card')
    client.objects.create(nome=nome, cpf=cpf, nasc=nasc, email=email, card=card)
    return render(request, 'mensagem.html', {'mensagem': 'cadastro de cliente efetuado com sucesso!', 'cod': 1})
def listcli(request):
    cli = client.objects.all()
    return render(request, 'listcli.html', {'cli': cli})
def editcli(request, id):
    user = client.objects.get(id=id)
    return render(request, 'editcli.html', {'user': user})

def confirmeditcli(request, id):
    user = client.objects.get(id=id)
    user.nome = request.POST.get('nome')
    user.email = request.POST.get('email')
    user.cpf = request.POST.get('cpf')
    user.nasc = request.POST.get('nasc')
    user.card = request.POST.get('card')
    user.save()
    return render(request, 'mensagem.html', {'mensagem': 'atualização de cliente efetuada com sucesso!', 'cod': 1, 'sit':'cli'})

def deletecli(request, id):
    user = client.objects.get(id=id)
    contaa = random.randrange(1, 100)
    contab = random.randrange(1, 100)
    return render(request, 'deletecli.html', context={'user':user, 'contaa':contaa, 'contab':contab})

def confirmdeletecli(request, id):
    contaa = int(request.POST.get('contaa'))
    contab = int(request.POST.get('contab'))
    calc = int(request.POST.get('calc'))
    conta = int(contaa+contab)
    if conta == calc:
        user = client.objects.get(id=id)
        user.delete()
        return render(request, 'mensagem.html', {'mensagem': 'cliente deletado com sucesso', 'cod': 1, 'sit':'cli'})
    else:
        return render(request, 'mensagem.html', {'mensagem': 'Resposta do cálculo incorreta.', 'cod': 0, 'sit':'cli'}) 
    
def teste(request):
    return render(request,'teste.html')

def inicio(request):
    return render(request, 'home.html')

def categorias(request):
    cat = categ.objects.all()
    return render(request, 'categorias.html', {'cat': cat})

def cadcateg(request):
    nome = request.POST.get('nome')
    categ.objects.create(nome=nome)
    cat = categ.objects.all()
    return render(request, 'categorias.html', {'cat': cat})

def deletecateg(request):
    cat = categ.objects.get(id=request.POST.get('id'))
    cat.delete()
    cat = categ.objects.all()
    return render(request, 'categorias.html', {'cat': cat})

def searchprod(request):
    id = request.POST.get('id')
    nome = request.POST.get('nome')
    prod = product.objects.filter(nome__contains=nome, id__contains=id)
    return render(request, 'listprod.html', {'prod': prod, 'cod': 1})
def searchcli(request):
    id = request.POST.get('id')
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    cli = client.objects.filter(id__contains=id, nome__contains=nome, cpf__contains=cpf)
    return render(request, 'listcli.html', {'cli':cli, 'cod':1})
