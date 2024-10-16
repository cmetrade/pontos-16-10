import pandas as pd 
import time
import os
os.system("awk {'print $1'} arquivos/usd-brl-segunda-abertura.txt arquivos/usd-brl-segunda-max.txt arquivos/usd-brl-segunda-min.txt > arquivos/usd-brl-segunda.txt")

with open("arquivos/usd-brl-segunda.txt", "r") as arquivo:
        result = arquivo.read()
print(result)
import requests
TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
chat_id = "-1001546918854"
message = "USD-BRL-SEGUNDA\n "
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {result}"
print(requests.get(url).json()) # this sends the message2