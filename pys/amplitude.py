import pandas as pd 
import time
import os

with open("arquivos/amplitude.txt", "r") as arquivo:
        arquivox = arquivo.read()

x = float(arquivox.replace('.','').replace(',','.'))
var1 = float(x)
number = 2 * var1
result = round(number, 3) 

print(result)
import requests
TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
chat_id = "-1001546918854"
message = "AMPLITUDE = "
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {result}"
print(requests.get(url).json()) # this sends the message