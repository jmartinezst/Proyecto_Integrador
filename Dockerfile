# Imagen base ligera
FROM python:3.11-slim

# Instalar dependencias del sistema para Tkinter
# 'tk-dev' es necesario para que la librería funcione en Linux
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app


# Copiar los archivos del proyecto
COPY . .

# Exponer puerto 
EXPOSE 8080 

# 8. Comando para ejecutar la aplicación
CMD ["python", "app.py"]