import requests
from bs4 import BeautifulSoup

#guardamos la URL en una variable
url = "https://books.toscrape.com/"

#hacemos la solicitud y la guardamos en respuesta ademas añadimos el encoding utf-8
respuesta = requests.get(url)
respuesta.encoding = "utf-8"

#verificamos que nos devuelva la respuesta 200, sino lanzamos error, y con soup lo parseamos a texto html,
#encontrando h3 y p respectivamente,luego los añadimos en un array que finalmente recorremos y añadimos como indice
if respuesta.status_code == 200:

    i = 0
    titulos = []
    preciosT = []

    soup = BeautifulSoup(respuesta.text, "html.parser")
    libros = soup.find_all("h3")

    for libro in libros:
        titulo = libro.find("a")["title"]
        titulos.append(titulo)

    precios = soup.find_all("p", "price_color")
    for precio in precios:
        precioL = precio.text
        preciosT.append(precioL)

    for i in range(len(titulos)):
        print(str(i) + "." + titulos[i] + " con precio " + preciosT[i])
        i += 1

else:
    print("hubo un error al obtener los libros")
