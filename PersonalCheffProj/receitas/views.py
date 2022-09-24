from django.shortcuts import render

def index(request):
    receitas = {
        1:'Suco de limão',
        2:'Suco de Laranja',
        3:'Torta de Frango',                       
    }

    dados = {
        'lista_receitas': receitas
    }
    return render(request, 'index.html', dados)

def contato(request):
    return render(request, 'contato.html')

def sucodelaranja(request):
    return render(request, 'sucodelaranja.html')

def sucodelimao(request):
    return render(request, 'sucodelimao.html')

def tortadefrango(request):
    return render(request, 'tortadefrango.html')


