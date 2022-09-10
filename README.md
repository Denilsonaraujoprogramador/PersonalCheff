# PersonalCheff
 APP para gerenciamento de receitas

 <!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
<img src="exemplo-image.png" alt="exemplo imagem">
> Uma aplicação web de receitas chamada PersonalCheff desenvolvida durante o curso de Python no Senac Americana. A aplicação listará receitas e clicando em cada nome de receita você pode ver a receita completa.
### Lista de tarefas
Segue a lista de tarefas a serem desenvolvidas no projeto:
-1 [X] Pré-requisitos
    - [X] Instalar o Python
    - [X] Instalar Visual Studio Code
<br><br>
-2 [X] Criar e ativar o ambiente virtual
```
python -m venv .\venv\
venv\Scripts\activate
```
-3 [X] Instalar o Django
```
pip install Django
ou para versão especifica nesse caso a versão 3.2, python -m pip install django==3.2
```
-4 [X] Criar o projeto PersonalCheff
```
django-admin startproject PersonalCheffProj
ou para questão de permissão inserir o ".py" no django-admin.py ficando da seguinte forma, django-admin.py startproject PersonalCheffProj
```
-5 [X] Abri a pasta PersonalCheffProj e subir o servidor e testar o projeto
```
cd PersonalCheffProj
python manage.py runserver
```
-6 [X] Alterar o idioma do projeto no arquivo settings.py para `pt-br`
-7 [X] Alterar o timezome do projeto no arquivo settings.py para `America/Sao_Paulo` 
<br><br>
-8 [X] Criar o app receitas
```
python manage.py startapp receitas
```
-9 [X] Registrar e adicionar o nome do app "receitas" no ***`settings.py >> INSTALLED_APPS`***
-10 [X] Adicionar arquivo urls.py no app receitas e Configurar a rota inicial do arquivo `urls.py`
-11 [x] Criar a `view` para rota inicial
-12 [x] Registrar a rota inicial
-13 [x] Dentro da pasta receitas(app), crie a pasta `templates`
-14 [x] Crie seus arquivos HTML  dentro da pasta templates do app 'receitas', começando pelo arquivo `index.hmtl`
-14.1 [x] No arquivo `views.py` que está dentro da paste do app `realize a seguite alteração para renderizar o arquivo index.html`:
    ```python
        from django.shortcuts import render

        def index(request):
            return render(request, 'index.html')
    ```
-14.2 [x] Crie o arquivo `sucodelaranja.hmtl`, dentro da pasta templates do app 'receitas'
-14.3 [x] No arquivo `views.py` que está dentro da paste do app `inclua a função que irá renderizar o arquivo sucodelaranja.html`:
    ```python
        def sucodelaranja(request):
            return render(request, 'sucodelaranja.html')
    ```

***!!ADICINAL IMPORANTE!!!! <br>
PADRÃO PARA CRIAR AS PÁGINAS (MODEL/VIEW/TEMPLATE) ITEM 14 CITADO ACIMA.*** <br>
<img src="passo_a_passo.png" alt="passo_a_passo">

-15 [x] <br>
    -Integrar arquivos estáticos (CSS, JS, IMG)
    - Dentro da pasta do projeto (PersonaCheffProj), criar a pasta `static` <br>
    -Dentro da pasta static, colocar as imagens, os arquivos CSS e Javascript (JS) conforme for utilizando. <br>
    -No arquivo `settings.py` realize a importação da biblioteca `import os` <br>
    -`No settings.py, menu TEMPLATES, submenu DIRS configure o caminho conforme abaixo e crie os menus STATIC_ROOT e  STATICFILES_DIRS:` <br>

    'DIRS': [os.path.join(BASE_DIR, 'receitas/templates')]

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'PersonalCheffProj/static')]

   -Execute o comando no terminal `python manage.py collectstatic` para organizar as pastas e arquivos CSS/JS/IMG automaticamente. <br><br> 
    -Na primeira linha dos arquivos seus arquivos HTML que possuirem arquivo státicos inclua sempre `{% load static %}`.
    -Insira imagem utilizando o comando, exemplo: `<img src="{% static 'logo.png'%}"`>. 

-16 [] Utilizando links

-17 [] Criando o base.html

-18 [] Separando em partials

-19 [] Renderizando dados dinamicamente

-20 [] Criando um dicionario com as receitas

-21 [] Criando o banco de dados(MySQL/MariaDB)

-22 [] Instalando o conector do bando de dados MySQL

-23 [] Criando o modelo da receita

-24 [] Criando a migration (mapeamento)

-25 [] Realizando a migration

-26 [] Registrando um modelo no admin

-27 [] Criando um usuário para o ambiente administrativo



<br><br>
## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
[⬆ Voltar ao topo](#nome-do-projeto)<br>

