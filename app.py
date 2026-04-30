# Importamos librerías necesarias
import json                       # Permite trabajar con archivos JSON (base de datos)
import tkinter as tk              # Librería para crear la interfaz gráfica
from tkinter import scrolledtext  # Widget de texto con scroll

# ---------------------------------------------------------
# FUNCIÓN: Cargar base de datos desde JSON
# ---------------------------------------------------------
def cargar_base_datos():
    try:
        # Abrimos el archivo JSON en modo lectura
        with open("base_datos.json", "r", encoding="utf-8") as file:
            return json.load(file)  # Convertimos JSON a diccionario Python
    except FileNotFoundError:
        # Si no existe el archivo, devolvemos estructura vacía
        return {"preguntas": []}

# ---------------------------------------------------------
# FUNCIÓN: Buscar respuesta en base de datos
# ---------------------------------------------------------
def buscar_respuesta_json(pregunta, base_datos):
    # Convertimos la pregunta del usuario en palabras clave
    palabras_pregunta = set(pregunta.lower().split())
    mejor_coincidencia = 0   # Guarda número de coincidencias
    mejor_item = None        # Guarda la mejor respuesta encontrada

    # Recorremos todas las preguntas del JSON
    for item in base_datos.get("preguntas", []):
        # Convertimos la pregunta del JSON en palabras clave
        palabras_clave = set(item.get("pregunta", "").lower().split())
        # Calculamos cuántas palabras coinciden
        coincidencias = len(palabras_clave.intersection(palabras_pregunta))
        # Nos quedamos con la que tenga MÁS coincidencias
        if coincidencias > mejor_coincidencia:
            mejor_coincidencia = coincidencias
            mejor_item = item

    # Si hay una coincidencia suficientemente buena (>= 2 palabras)
    if mejor_item and mejor_coincidencia >= 2:
        respuesta = mejor_item.get("respuesta", "Respuesta no disponible")
        url = mejor_item.get("url", "No disponible")
        return f"{respuesta}\nMás información: {url}"

    # Si no encuentra nada útil
    return "Lo siento, no tengo una respuesta para esa pregunta."

# ---------------------------------------------------------
# FUNCIÓN: Obtener respuesta (cuando el usuario pulsa botón)
# ---------------------------------------------------------
def obtener_respuesta():
    pregunta = entrada_usuario.get()
    if pregunta.strip() == "":
        return
    respuesta = buscar_respuesta_json(pregunta, base_datos)
    historial_texto.insert(
        tk.END,
        f"Tú: {pregunta}\nChatbot: {respuesta}\n\n"
    )
    entrada_usuario.delete(0, tk.END)

# CARGA INICIAL DE DATOS
base_datos = cargar_base_datos()

# ---------------------------------------------------------
# INTERFAZ GRÁFICA (Tkinter)
# ---------------------------------------------------------
root = tk.Tk()
root.title("Chatbot con Tkinter y Base de Datos")

# ÁREA DE TEXTO (historial del chat)
historial_texto = scrolledtext.ScrolledText(
    root, width=50, height=20, wrap=tk.WORD
)
historial_texto.pack(pady=10)

# CAMPO DE ENTRADA DEL USUARIO
entrada_usuario = tk.Entry(root, width=50)
entrada_usuario.pack(pady=5)

# BOTÓN ENVIAR
boton_enviar = tk.Button(
    root, text="Enviar", command=obtener_respuesta
)
boton_enviar.pack(pady=5)

# BUCLE PRINCIPAL
root.mainloop()