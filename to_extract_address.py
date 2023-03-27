# -*- coding: utf-8 -*-
"""to_extract_address.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PPtTz73m_Me51kyypwu92MIl568cdcjX
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

df = pd.read_excel('Web Scraping Assignment.xlsx')

df.fillna('0', inplace=True)

link_list = df[' WEBSITE']
link_list.head()

addresses = []

for i in link_list:
  if i != '0':
    # print(i)
    url = i
    # Send a GET request to the URL and retrieve the HTML content
    try: 
      response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
      addresses.append("didn't get a response")
      continue
    html_content = response.content

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the element(s) that contain the college address
    address_elements = soup.find_all('address')

    # Extract the address text from the element(s)
    address = ''
    if len(address_elements) > 0:
      address = address_elements[0].get_text()
    addresses.append(address)
  else:
    addresses.append('None')
  len(addresses)

addresses

df['ADDRESS'] = addresses

df.to_excel('New_excel.xlsx')

