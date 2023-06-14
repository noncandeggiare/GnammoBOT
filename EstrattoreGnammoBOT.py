#GnammoBOT

import requests
from bs4 import BeautifulSoup
import datetime

# Get today's date
today = datetime.date.today()

# Variables for comune and grado
comune = 7
grado = 2

# URL for the catering menu with variables
url = f"https://www.mazzotti.org/bassaromagnacatering/calendar.php?comune={comune}&grado={grado}&giorno={today}"

# Send a GET request to the URL with certificate verification disabled
response = requests.get(url, verify=False)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the div element with the class "fc-day-number" containing today's day number
day_element = soup.find("div", class_="fc-day-number", text=str(today.day))

# Find the parent div element with class "fc-div-content"
div_content_element = day_element.find_parent("div", class_="fc-div-content")

# Find the nested div element with class "menu-calendar"
menu_element = div_content_element.find("div", class_="menu-calendar")

# Check if menu is available for today
if menu_element is not None:
    # Extract the menu text
    menu_text = menu_element.get_text(separator="\n").strip()
    print("Menu for today:")
    print(menu_text)
else:
    print("No menu available for today.")