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
- [] Instalar o Django
```
pip install Django
ou para versão especifica nesse caso a versão 3.2, python -m pip install django==3.2
```
- [] Criar o projeto PersonalCheff
```
django-admin startproject PersonalCheffProj
ou para questão de permissão inserir o ".py" no django-admin.py ficando da seguinte forma, django-admin.py startproject PersonalCheffProj
```
- [] Abri a pasta PersonalCheffProj e Subir o servidor e testar o projeto
```
cd PersonalCheffProj
python manage.py runserver
```
- [] Alterar o idioma do projeto para `pt-br`
- [] Alterar o timezome do projeto para `America/Sao_Paulo` <br><br>
- [] Criar o app receitas
```
python manage.py startapp
```
- [] Registrar o app receitas no ***`settings`***
- [] Configurar a rota inicial na `urls.py`
- [] Criar a `view` para rota inicial
- [] Registrar a rota inicial
- [] Criar o arquivo index.html

## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
[⬆ Voltar ao topo](#nome-do-projeto)<br>

