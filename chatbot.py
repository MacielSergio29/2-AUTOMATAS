import tkinter as tk
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import sqlite3
import wikipediaapi
from forex_python.converter import CurrencyRates

# Configuración de la base de datos
conn = sqlite3.connect('chatbot.db')
cursor = conn.cursor()

# Crear una tabla para almacenar conversaciones si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_input TEXT,
    bot_response TEXT
)
''')

def guardar_conversacion(user_input, bot_response):
    cursor.execute('''
    INSERT INTO conversations (user_input, bot_response)
    VALUES (?, ?)
    ''', (user_input, bot_response))
    conn.commit()

# Crear una nueva instancia de un chatbot
chatbot = ChatBot('Simple Bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish")

# Función para convertir divisas
c = CurrencyRates()

def convertir_moneda(cantidad, from_currency, to_currency):
    try:
        resultado = c.convert(from_currency.upper(), to_currency.upper(), float(cantidad))
        return f"{cantidad} {from_currency.upper()} son {resultado:.2f} {to_currency.upper()}"
    except:
        return "Error en la conversión de moneda."

# Función para buscar en Wikipedia
wiki = wikipediaapi.Wikipedia('es')

def buscar_wikipedia(termino):
    page = wiki.page(termino)
    if page.exists():
        return page.summary[:2000]  # Limitar la respuesta a 2000 caracteres
    else:
        return "No se encontró información sobre ese término en Wikipedia."

def enviar():
    user_input = entry.get()
    entry.delete(0, tk.END)
    
    if user_input.lower().startswith("convierte"):
        partes = user_input.split()
        cantidad, from_currency, to_currency = partes[1], partes[2], partes[3]
        response = convertir_moneda(cantidad, from_currency, to_currency)
    elif user_input.lower().startswith("busca"):
        termino = user_input[len("busca "):]
        response = buscar_wikipedia(termino)
    else:
        bot_response = chatbot.get_response(user_input)
        response = bot_response.text
        guardar_conversacion(user_input, response)
    
    text_area.insert(tk.END, "Tú: " + user_input + "\n")
    text_area.insert(tk.END, "Bot: " + response + "\n")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("ChatBot")

text_area = tk.Text(root, height=20, width=50)
text_area.pack()

entry = tk.Entry(root, width=50)
entry.pack()

send_button = tk.Button(root, text="Enviar", command=enviar)
send_button.pack()

root.mainloop()