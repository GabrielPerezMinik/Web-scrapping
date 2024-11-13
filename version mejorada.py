import requests
from bs4 import BeautifulSoup
import time

url = "https://books.toscrape.com/"

start_time = time.time()
# Hacer la solicitud HTTP
respuesta = requests.get(url)
respuesta.encoding = "utf-8"

# Verificar que la respuesta es exitosa
if respuesta.status_code == 200:

    # Inicializar listas para almacenar títulos y precios
    titulos = []
    preciosT = []

    # Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(respuesta.text, "html.parser")

    # Extraer los títulos
    libros = soup.find_all("h3")
    for libro in libros:
        titulos.append(libro.find("a")["title"])

    # Extraer los precios
    precios = soup.find_all("p", class_="price_color")
    for precio in precios:
        preciosT.append(precio.text.strip())  # Usamos strip() para limpiar espacios innecesarios

    i = 1
    # Imprimir los títulos con sus precios
    for titulo, precio in zip(titulos, preciosT):
        print(f"{i}. {titulo} con precio {precio}")
        i += 1

else:
    print("Hubo un error al obtener los libros.")

# Medir el tiempo de fin
end_time = time.time()

# Calcular el tiempo transcurrido
execution_time = end_time - start_time
print(f"El programa tardó {execution_time:.2f} segundos en ejecutarse.")