from bs4 import BeautifulSoup
from urllib import request
import pandas as pd
import requests
import os

url = requests.get('https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue').text
soup = BeautifulSoup(url, 'lxml')

table = soup.find('table', {'class': 'wikitable sortable'})
table_rows = table.find_all('tr')


data = []
for row in table_rows:
	data.append([t.text.strip() for t in row.find_all('td')])


df = pd.DataFrame(data[2:], columns=['Rank','Name', 'Industry', 'Revenue', 'Profit', 'Employees', 'Country'],)
