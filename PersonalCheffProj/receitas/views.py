from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sucodelaranja(request):
    return render(request, 'sucodelaranja.html')

def sucodelimao(request):
    return render(request, 'sucodelimao.html')

def tortadefrango(request):
    return render(request, 'tortadefrango.html')

def bolodechocolate(request):
    return render(request, 'bolodechocolate.html')
