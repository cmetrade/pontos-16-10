import pandas as pd 
import time
import os

with open("arquivos/dx-fechamento.txt", "r") as dxfecha:
     dx = dxfecha.read()

with open("arquivos/dx-min.txt", "r") as dxmin:
        dxminima = dxmin.read()


fechamento = float(dx.replace('.','').replace(',','.'))
min = float(dxminima.replace('.','').replace(',','.'))


numero = (min - fechamento) / fechamento  
rounded_numero = round(numero, 3)

with open("arquivos/wdo-fecha.txt", "r") as arquivo:
        x = arquivo.read()

#wdo = float(x) 
wdo = float(x.replace('.','').replace(',','.'))
dxminima = rounded_numero
number = wdo * (dxminima+1)
rounded_number = round(number, 2)
print(rounded_number)
result = rounded_number

import requests
TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
chat_id = "-1001546918854"
message = "DX MÍNIMA = "
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {result}"
print(requests.get(url).json()) # this sends the message