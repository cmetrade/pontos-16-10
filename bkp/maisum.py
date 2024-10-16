import pandas as pd 
import time
import os


with open("arquivos/fechamentoWDO.txt", "r") as arquivo:
        x = arquivo.read()

wdo = float(x.replace('.','').replace(',','.'))
num1 = wdo * 0.01
number = wdo + num1
rounded_number = round(number, 1)
print(rounded_number)
result = rounded_number

import requests
TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
chat_id = "-1001546918854"
message = "MAIS UM = "
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {result}"
print(requests.get(url).json()) # this sends the messageiola 