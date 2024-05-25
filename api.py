from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import sqlite3
import wikipediaapi
from forex_python.converter import CurrencyRates

app = Flask(__name__)

# Configuración de la base de datos
conn = sqlite3.connect('chatbot.db', check_same_thread=False)
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

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
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
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)