# Chatbot de Comandos Docker 
> Chatbot interactivo desarrollado con Python, Tkinter y Docker.

## Descripción del proyecto
Este proyecto es un chatbot educativo diseñado para responder dudas sobre comandos de Docker. Utiliza **Tkinter** para la interfaz gráfica y un archivo **JSON** como base de datos ligera. 

El objetivo principal es demostrar habilidades en:
* Desarrollo con Python.
* Gestión de datos en JSON.
* Contenerización con **Docker**.
* Orquestación con **Docker Compose**.

## Funcionalidades
- **Interfaz Gráfica**: Ventana de escritorio con historial de conversación y scroll.
- **Base de Datos JSON**: Fácil de actualizar y mantener.
- **Motor de búsqueda**: Lógica basada en coincidencias de palabras clave.

## Requisitos
* Python 3.x
* Docker & Docker Compose
* Un servidor X11 (si usas Linux) o XQuartz (si usas macOS) para ver la GUI.

## Despliegue con Docker
El proyecto está configurado para ejecutarse totalmente contenido:

- **Dockerfile**: Basado en `python:3.11-slim`, incluye las dependencias de sistema para Tkinter y ejecuta la app automáticamente.
- **Docker Compose**: Gestiona el servicio, monta volúmenes para el JSON y configura las variables de entorno necesarias para la interfaz gráfica.

### Cómo ejecutar:
```bash
# Clonar el repo
git clone <tu-url-del-repo>

# Levantar con Docker Compose
docker-compose up --build