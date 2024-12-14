import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns


# Seleccionar el recurso a descargar
resource_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Petición para descargar el fichero de Internet
response = requests.get(resource_url, time.sleep (10))

# Si la petición se ha ejecutado correctamente (código 200), entonces el contenido HTML de la página se ha podido descargar
if response == 200:
    # Transformamos el HTML plano en un HTML real (estructurado y anidado, con forma de árbol)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup




