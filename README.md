# 🐍 Tutorial Oficial de Django - Proyecto Inicial

Este repositorio sigue el tutorial oficial de Django en español:  
🔗 https://docs.djangoproject.com/es/stable/intro/tutorial01/

El objetivo es aprender a crear un proyecto básico con Django, utilizando un entorno virtual, configurando una app, y ejecutando un servidor de desarrollo.

---

## 📦 Requisitos

- Python 3.8 o superior
- pip
- Entorno virtual (`venv`)

---

## ⚙️ 1. Crear un entorno virtual

Desde la terminal o PowerShell:

```bash
python -m venv env

Activar el entorno:

En Windows: env\Scripts\activate

2. Instalar Django
Una vez activado el entorno virtual:

bash
pip install django
Verificar que se instaló correctamente:

bash
django-admin --version

3. Crear un nuevo proyecto
bash

# django-admin startproject mysite
cd mysite
mysite/
├── manage.py
└── mysite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py

▶️ 4. Ejecutar el servidor de desarrollo
bash
python manage.py runserver
http://127.0.0.1:8000/
5. Crear una aplicación

bash
python manage.py startapp polls

polls/
├── admin.py
├── apps.py
├── migrations/
├── models.py
├── tests.py
├── views.py
└── __init__.py

#Registrar la app polls en mysite/settings.py:
En polls/views.py:
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, estás en la app de encuestas.")

#Crear el archivo polls/urls.py:
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

#Editar mysite/urls.py para incluir las URLs de la app:
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

## Ver resultado
http://127.0.0.1:8000/polls/

Hola, estás en la app de encuestas.

## Próximos pasos (Tutorial 2 en adelante)

Crear modelos y usar base de datos
Configurar el panel de administración
Agregar templates
Formularios y vistas genéricas

