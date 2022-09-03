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
- [X] Pré-requisitos
    - [X] Instalar o Python
    - [X] Instalar Visual Studio Code
<br><br>
- [X] Criar e ativar o ambiente virtual
```
python -m venv .\venv\
venv\Scripts\activate
```
- [X] Instalar o Django
```
pip install Django
ou para versão especifica nesse caso a versão 3.2, python -m pip install django==3.2
```
- [X] Criar o projeto PersonalCheff
```
django-admin startproject PersonalCheffProj
ou para questão de permissão inserir o ".py" no django-admin.py ficando da seguinte forma, django-admin.py startproject PersonalCheffProj
```
- [X] Abri a pasta PersonalCheffProj e subir o servidor e testar o projeto
```
cd PersonalCheffProj
python manage.py runserver
```
- [X] Alterar o idioma do projeto no arquivo settings.py para `pt-br`
- [X] Alterar o timezome do projeto no arquivo settings.py para `America/Sao_Paulo` 
<br><br>
- [X] Criar o app receitas
```
python manage.py startapp receitas
```
- [X] Registrar e adicionar o nome do app "receitas" no ***`settings.py >> INSTALLED_APPS`***
- [X] Adicionar arquivo urls.py no app receitas e Configurar a rota inicial do arquivo `urls.py`
- [x] Criar a `view` para rota inicial
- [x] Registrar a rota inicial
- [x] Dentro da pasta receitas(app), crie a pasta `templates`
- [x] Crie seus arquivos HTML começando pelo arquivo `index.hmtl`, dentro da pasta templates do app 'receitas'
- [x] No arquivo `views.py` que está dentro da paste do app `realize a seguite alteração para renderizar o arquivo index.html`:
    ```python
        from django.shortcuts import render

        def index(request):
            return render(request, 'index.html')
    ```
- [x] Crie o arquivo `sucodelaranja.hmtl`, dentro da pasta templates do app 'receitas'
- [x] No arquivo `views.py` que está dentro da paste do app `inclua a função abaixo para renderizar o arquivo sucodelaranja.html`:
    ```python
        def sucodelaranja(request):
            return render(request, 'sucodelaranja.html')
    ```



## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
[⬆ Voltar ao topo](#nome-do-projeto)<br>

