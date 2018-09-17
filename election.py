# import libraries
import requests
from bs4 import BeautifulSoup

# Collect and parse first page
page = requests.get('https://www.politico.com/2016-election/results/map/president/texas/')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='content-alpha')
print(artist_name_list)
# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('th')

artist_name_list = soup.find(class_='results-name')
artist_name_list_items = artist_name_list.find_all('span')

# Create for loop to print out all artists' names
for artist_name in artist_name_list_items:
      print(artist_name.prettify())