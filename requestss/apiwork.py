import requests
def convert():
    value = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    while True:
        try:
            vav= input('write the currency you are interested in (for example: USD, KZT, EUR) ').upper()
            us=value['Valute'][vav]
            cena=us['Value']
            nominal=us['Nominal']
            return cena, vav, nominal
        except KeyError:
            print('not found in cb')
cena, vav, nominal = convert()
while True:
    try:
        amount = int(input(f'how much {vav} to rub? '))
        break
    except ValueError:
        print('only digits!')  
cena = (cena / nominal)  
print(f'{amount} {vav} = {round(amount*cena, 2)} rubles')
