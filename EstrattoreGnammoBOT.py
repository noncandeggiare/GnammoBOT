# GnammoBOT

import requests
import BeautifulSoup

# URL del sito
url = "https://www.mazzotti.org/bassaromagnacatering/"

# Parametri per la selezione del menu
comune_value = "Massa Lombarda"
grado_value = "Infanzia"
data_value = "2023-06-13"  # Sostituisci con la data desiderata nel formato "AAAA-MM-GG"

# Costruisci il payload per la richiesta POST
payload = {
    "comune": comune_value,
    "grado": grado_value,
    "giorno": data_value
}

# Effettua la richiesta POST per ottenere il menu
response = requests.post(url, data=payload)

# Analizza il contenuto HTML della risposta
soup = BeautifulSoup(response.text, "html.parser")

# Trova il menu del giorno
menu_elements = soup.select("div.container-fluid div.row div.col-sm-6.menu div.row div.col-xs-8.data")

# Estrai il testo del menu
menu = [menu_element.text.strip() for menu_element in menu_elements]

# Stampa il menu
for item in menu:
    print(item)