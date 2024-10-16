# importing pandas module 
import pandas as pd 
import os

# Valores e alta do CME
with open("arquivos/cme-low.txt", "r") as high:
        x1 = high.read()

with open("arquivos/cme-low-old.txt", "r") as highold:
        x2 = highold.read()

var1 = float(x1)
number1 = 1 / var1
alta1 = round(number1, 4) 

var2 = float(x2)
number2 = 1 / var2
alta2 = round(number2, 4) 

# Valores e baixa do CME

with open("arquivos/cme-high.txt", "r") as low:
        x3 = low.read()

with open("arquivos/cme-high-old.txt", "r") as lowold:
        x4 = lowold.read()

var3 = float(x3)
number3 = 1 / var3
baixa1 = round(number3, 4) 

var4 = float(x4)
number4 = 1 / var4
baixa2 = round(number4, 4) 


if alta1 != alta2:
    print('O valor do CME é {:.3f}'.format(alta1))
    import requests
    TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
    chat_id = "-1001546918854"
    message = "CME de alta alterado para"
    result = '{:.3f}'.format(alta1)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {result}"
    print(requests.get(url).json()) # this sends the message
    pass

else:
    print("igual")


if baixa1 != baixa2:
    print('O valor do CME é {:.3f}'.format(baixa1))
    import requests
    TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
    chat_id = "-1001546918854"
    message = "CME de baixa alterado para"
    result = '{:.3f}'.format(baixa1)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {result}"
    print(requests.get(url).json()) # this sends the message
    pass

else:
    print("igual")    
