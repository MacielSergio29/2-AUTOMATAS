import unittest
from forex_python.converter import CurrencyRates
import wikipediaapi

c = CurrencyRates()

def convertir_moneda(cantidad, from_currency, to_currency):
    try:
        resultado = c.convert(from_currency.upper(), to_currency.upper(), float(cantidad))
        return f"{cantidad} {from_currency.upper()} son {resultado:.2f} {to_currency.upper()}"
    except:
        return "Error en la conversión de moneda."

wiki = wikipediaapi.Wikipedia('es')

def buscar_wikipedia(termino):
    page = wiki.page(termino)
    if page.exists():
        return page.summary[:2000]  # Limitar la respuesta a 2000 caracteres
    else:
        return "No se encontró información sobre ese término en Wikipedia."

class TestChatBot(unittest.TestCase):

    def test_convertir_moneda(self):
        self.assertIn("USD son", convertir_moneda(100, 'USD', 'MXN'))
        self.assertIn("EUR son", convertir_moneda(50, 'EUR', 'MXN'))
        self.assertEqual(convertir_moneda(100, 'USD', 'INVALIDO'), "Error en la conversión de moneda.")

    def test_buscar_wikipedia(self):
        self.assertIn("es una enciclopedia", buscar_wikipedia("Wikipedia"))
        self.assertEqual(buscar_wikipedia("Un término que no existe en Wikipedia"), "No se encontró información sobre ese término en Wikipedia.")

if __name__ == '__main__':
    unittest.main()