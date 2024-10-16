import pandas as pd 
import time
import os

os.system("awk {'print $1'} arquivos/ptax-futuro.txt > arquivos/ptax-futuro2.txt")
with open("arquivos/ptax.txt", "r") as arquivo:
        ptax1 = arquivo.read()
with open("arquivos/ptax-futuro2.txt", "r") as arquivo:
        ptax2 = arquivo.read()
import requests
TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
chat_id = "-1001546918854"
message = "PTAX-FUTURO = "
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {ptax1} {ptax2}"
print(requests.get(url).json()) # this sends the message