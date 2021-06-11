# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:05:55 2021

@author: hnrne
"""

from bs4 import BeautifulSoup  
import requests 
import requests
import json
import pandas as pd
import xlwings as xw
from df2gspread import df2gspread as d2g
import gspread  
  
url="https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY" 
  
# Make a GET request to fetch the raw HTML content  
html_content = requests.get(url).text  
  
# Parse the html content  
soup = BeautifulSoup(html_content, "html5lib")  
print(soup.prettify()) # print the parsed data of html  
print(soup.title)
result=requests.get("https://www.nseindia.com/option-chain")
assert result.content
table=document.find("div")
table
assert table.find("div")
new_url = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'

headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(new_url,headers=headers)
dajs = json.loads(page.text)


def fetch_oi(expiry_dt):
    ce_values = [data['CE'] for data in dajs['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
    pe_values = [data['PE'] for data in dajs['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]

    ce_dt = pd.DataFrame(ce_values).sort_values(['strikePrice'])
    pe_dt = pd.DataFrame(pe_values).sort_values(['strikePrice'])
    
    print(ce_dt[['strikePrice','lastPrice']])

def main():
    
    expiry_dt = '27-Aug-2020'
    fetch_oi(expiry_dt)

if __name__ == '__main__':
    main()