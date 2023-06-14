#GnammoBOT

import requests
from bs4 import BeautifulSoup
import datetime

# Get today's date
today = datetime.date.today()


# URL for the catering menu
url = f"https://www.mazzotti.org/bassaromagnacatering/calendar.php?comune=7&grado=2&giorno={today}"

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

import requests
from bs4 import BeautifulSoup

# URL for the catering menu
url = "https://www.mazzotti.org/bassaromagnacatering/calendar.php?comune=7&grado=2&giorno=2023-06-13"

# Send a GET request to the URL
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
    menu_text = menu_element.get_text(separator="\n")
    menu_text = menu_text.strip()  # Remove leading/trailing whitespaces
    menu_text = menu_text.replace('\n', '<br>')  # Replace line breaks with <br> tags

    # Create the HTML content
    html_content = f"<html><body><p>Oggi si mangia:</p><p>{menu_text}</p></body></html>"

    # Save the HTML content to output.html file
    with open("output.html", "w") as file:
        file.write(html_content)
else:
    with open("output.html", "w") as file:
        file.write("<html><body><p>No menu available for today.</p></body></html>")