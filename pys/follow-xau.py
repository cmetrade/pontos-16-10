# importing pandas module 
import pandas as pd 
import os

# xau alta
with open("arquivos/xau-fechamento.txt", "r") as xaufecha:
     xau = xaufecha.read()

with open("arquivos/xau-max.txt", "r") as xaumax:
        xaumaxima = xaumax.read()


fechamento = float(xau.replace('.','').replace(',','.'))
max = float(xaumaxima.replace('.','').replace(',','.'))


numero = (max - fechamento) / fechamento  
rounded_numero = numero

with open("arquivos/wdo-fecha.txt", "r") as arquivo:
        x = arquivo.read()

wdo = float(x.replace('.','').replace(',','.'))
xaualta = rounded_numero
number = wdo * (xaualta+1)
rounded_number = number
print(rounded_number)
result_max = rounded_number

# xau ALTA OLD
with open("arquivos/xau-max-old.txt", "r") as xaumax_old:
        xaumaxima_old = xaumax_old.read()


max_old = float(xaumaxima_old.replace('.','').replace(',','.'))


numero_old = (max_old - fechamento) / fechamento  
rounded_numero_old = numero_old

with open("arquivos/wdo-fecha.txt", "r") as arquivo_old:
        x_old = arquivo_old.read()

wdo_old = float(x_old.replace('.','').replace(',','.'))
xaualta_old = rounded_numero_old
number_old = wdo_old * (xaualta_old+1)
rounded_number_old = number_old
print(rounded_number_old)
result_max_old = rounded_number_old


if result_max != result_max_old:
    print('O valor do xau MAX é {:.3f}'.format(result_max))
    import requests
    TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
    chat_id = "-1001546918854"
    message = "xau de alta alterado para"
    result = '{:.3f}'.format(result_max)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {result_max}"
    print(requests.get(url).json()) # this sends the message
    pass

else:
    print("igual")

#######
    
# xau BAIXA

with open("arquivos/xau-min.txt", "r") as xaumin:
        xauminima = xaumin.read()

min = float(xauminima.replace('.','').replace(',','.'))


numero_min = (min - fechamento) / fechamento  
rounded_numero_min = numero_min

with open("arquivos/wdo-fecha.txt", "r") as arquivo_min:
        x_min = arquivo_min.read()

wdo_min = float(x_min.replace('.','').replace(',','.'))
xaubaixa = rounded_numero_min
number_min = wdo_min * (xaubaixa+1)
rounded_number_min = number_min
print(rounded_number_min)
result_min = rounded_number_min

# xau BAIXA OLD
with open("arquivos/xau-min-old.txt", "r") as xaumin_old:
        xauminima_old = xaumin_old.read()


min_old = float(xauminima_old.replace('.','').replace(',','.'))


numero_min_old = (min_old - fechamento) / fechamento  
rounded_numero_min_old = numero_min_old

with open("arquivos/wdo-fecha.txt", "r") as arquivo_min_old:
        x_min_old = arquivo_min_old.read()

wdo_min_old = float(x_min_old.replace('.','').replace(',','.'))
xaubaixa_old = rounded_numero_min_old
number_min_old = wdo_min_old * (xaubaixa_old+1)
rounded_number_min_old = number_min_old
print(rounded_number_min_old)
result_min_old = rounded_number_min_old


if result_min != result_min_old:
    print('O valor do xau MIN é {:.3f}'.format(result_min))
    import requests
    TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
    chat_id = "-1001546918854"
    message = "xau de baixa alterado para"
    result = '{:.3f}'.format(result_min)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {result_min}"
    print(requests.get(url).json()) # this sends the message
    pass

else:
    print("igual")   
