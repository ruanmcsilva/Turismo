from django.shortcuts import render
from .models.destinos import Destinos
from .models.passeio import Passeio
from .models.ecologica import Ecologica
from .models.pousada import Pousada
from .models.carros import Aluguel
from .models.negociar import Negociar
# Create your views here.

def viagens_list (request):
   viagens = Destinos.objects.select_related('agencia').all()
   context = {'viagens':viagens}
   return render(request, 'viagens/index.html', context)

def viagens_description(request,pk):
   local = Destinos.objects.get(pk=pk)
   context = {'local':local}
   return render(request, 'viagens/descricao.html', context)

def passeio_list(request):
   passeio = Passeio.objects.all()
   context = {'passeio':passeio}
   return render(request, 'viagens/passeios.html', context)

def ecologica_list(request):
   rota = Ecologica.objects.all()
   context = {'rota':rota}
   return render(request, 'viagens/rota.html', context)

def pousada_description(request):
   pousada = Pousada.objects.first()
   context = {'pousada':pousada}
   return render(request, 'viagens/pousada.html', context)

def carros_list(request):
   carro = Aluguel.objects.all()
   context = {'carro':carro}
   return render(request, 'viagens/veiculos.html', context)

def carros_description(request,pk): #adicionei aqui, a mesma coisa de uma view de cima
   veiculos = Aluguel.objects.get(pk=pk)
   context = {'veiculos':veiculos}
   return render(request, 'viagens/descricaocarro.html', context)

def contato_description(request):
   negociar = Negociar.objects.all()
   context = {'negociar':negociar}
   return render(request, 'viagens/contato.html', context)

def passeios_description(request,pk): #adicionei aqui, a mesma coisa de uma view de cima
   passeios = Passeio.objects.get(pk=pk)
   context = {'passeios':passeios}
   return render(request, 'viagens/descricaopasseio.html', context)
