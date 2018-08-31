import os
import numbers
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://www.x-rates.com/table/?from=USD&amount=1'

#Web Scraping
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
table = soup.find('')

listRows = []
currencies = {}
for row in table.findAll('tr'):                                 #List of rows
    listCells = []
    for cell in row.findAll('td'):                              #Individual Data Cells
        listCells.append(cell.text)
    if(len(listCells) == 3):
        listRows.append(listCells)
        currencies[listCells[0]] = listCells[1]

#Inserting rows into a map
print('\nHello user! Welcome to the currency converter!\n')
input = raw_input('Would you like to see a list of current supported currencies w/conversion rates from 1.00 USD? (y or n) \n')
if(input == 'Y' or input == 'y'):   #Printing out conversion rates with currencies
    print('\nCurrently Supported Currencies (and rates comparative to 1.00 USD):\n')
    for key, value in currencies.items():
        print key, ': ', value
    print('')

#User input
while(True):
    currencyInput = raw_input('\nEnter the name (Capitalized and spelled correctly) of the currency you would like to convert US dollars to!\n')
    if(currencyInput in currencies):
        #Getting conversion ammount
        while(True):
            try:
                currencyAmmount = float(raw_input('\nEnter the ammount of USD to convert to ' + currencyInput + '!\n'))
                val = float(currencies[currencyInput])
                calculated = val * currencyAmmount
                print('\n' + str(currencyAmmount) + ' USD is '+ str(calculated) + ' ' + str(currencyInput) + 's\n')
                break;
            except:
                print('Not an integer, try again!\n');
        break;
    else:
        print('Invalid Response! Try again!\n')

