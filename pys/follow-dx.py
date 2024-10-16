# importing pandas module 
import pandas as pd 
import os

# DX alta
with open("arquivos/dx-fechamento.txt", "r") as dxfecha:
     dx = dxfecha.read()

with open("arquivos/dx-max.txt", "r") as dxmax:
        dxmaxima = dxmax.read()


fechamento = float(dx.replace('.','').replace(',','.'))
max = float(dxmaxima.replace('.','').replace(',','.'))


numero = (max - fechamento) / fechamento  
rounded_numero = numero

with open("arquivos/wdo-fecha.txt", "r") as arquivo:
        x = arquivo.read()

wdo = float(x.replace('.','').replace(',','.'))
dxalta = rounded_numero
number = wdo * (dxalta+1)
rounded_number = number
print(rounded_number)
result_max = rounded_number

# DX ALTA OLD
with open("arquivos/dx-max-old.txt", "r") as dxmax_old:
        dxmaxima_old = dxmax_old.read()


max_old = float(dxmaxima_old.replace('.','').replace(',','.'))


numero_old = (max_old - fechamento) / fechamento  
rounded_numero_old = numero_old

with open("arquivos/wdo-fecha.txt", "r") as arquivo_old:
        x_old = arquivo_old.read()

wdo_old = float(x_old.replace('.','').replace(',','.'))
dxalta_old = rounded_numero_old
number_old = wdo_old * (dxalta_old+1)
rounded_number_old = number_old
print(rounded_number_old)
result_max_old = rounded_number_old


if result_max != result_max_old:
    print('O valor do DX MAX é {:.3f}'.format(result_max))
    import requests
    TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
    chat_id = "-1001546918854"
    message = "DX de alta alterado para"
    result = '{:.3f}'.format(result_max)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {result_max}"
    print(requests.get(url).json()) # this sends the message
    pass

else:
    print("igual")

#######№#####################################№#####################################№##############################
    
# DX BAIXA

with open("arquivos/dx-min.txt", "r") as dxmin:
        dxminima = dxmin.read()

min = float(dxminima.replace('.','').replace(',','.'))


numero_min = (min - fechamento) / fechamento  
rounded_numero_min = numero_min

with open("arquivos/wdo-fecha.txt", "r") as arquivo_min:
        x_min = arquivo_min.read()

wdo_min = float(x_min.replace('.','').replace(',','.'))
dxbaixa = rounded_numero_min
number_min = wdo_min * (dxbaixa+1)
rounded_number_min = number_min
print(rounded_number_min)
result_min = rounded_number_min

# DX BAIXA OLD
with open("arquivos/dx-min-old.txt", "r") as dxmin_old:
        dxminima_old = dxmin_old.read()


min_old = float(dxminima_old.replace('.','').replace(',','.'))


numero_min_old = (min_old - fechamento) / fechamento  
rounded_numero_min_old = numero_min_old

with open("arquivos/wdo-fecha.txt", "r") as arquivo_min_old:
        x_min_old = arquivo_min_old.read()

wdo_min_old = float(x_min_old.replace('.','').replace(',','.'))
dxbaixa_old = rounded_numero_min_old
number_min_old = wdo_min_old * (dxbaixa_old+1)
rounded_number_min_old = number_min_old
print(rounded_number_min_old)
result_min_old = rounded_number_min_old


if result_min != result_min_old:
    print('O valor do DX MIN é {:.3f}'.format(result_min))
    import requests
    TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
    chat_id = "-1001546918854"
    message = "DX de baixa alterado para"
    result = '{:.3f}'.format(result_min)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {result_min}"
    print(requests.get(url).json()) # this sends the message
    pass

else:
    print("igual")   

#######№#####################################№#####################################№###########################
    
#DX ABERTURA

with open("arquivos/dx-abertura.txt", "r") as dxabe:
        dxabertura = dxabe.read()

abe = float(dxabertura.replace('.','').replace(',','.'))


numero_abe = (abe - fechamento) / fechamento  
rounded_numero_abe = numero_abe

with open("arquivos/wdo-fecha.txt", "r") as arquivo_abe:
        x_abe = arquivo_abe.read()

wdo_abe = float(x_abe.replace('.','').replace(',','.'))
dxopen = rounded_numero_abe
number_abe = wdo_abe * (dxopen+1)
rounded_number_abe = number_abe
print(rounded_number_abe)
result_abe = rounded_number_abe

# DX ABERTURA OLD
with open("arquivos/dx-abertura-old.txt", "r") as dxabe_old:
        dxabertura_old = dxabe_old.read()


abe_old = float(dxabertura_old.replace('.','').replace(',','.'))


numero_abe_old = (abe_old - fechamento) / fechamento  
rounded_numero_abe_old = numero_abe_old

with open("arquivos/wdo-fecha.txt", "r") as arquivo_abe_old:
        x_abe_old = arquivo_abe_old.read()

wdo_abe_old = float(x_abe_old.replace('.','').replace(',','.'))
dxopen_old = rounded_numero_abe_old
number_abe_old = wdo_abe_old * (dxopen_old+1)
rounded_number_abe_old = number_abe_old
print(rounded_number_abe_old)
result_abe_old = rounded_number_abe_old


if result_abe != result_abe_old:
    print('O valor do DX ABERTURA é {:.3f}'.format(result_min))
    import requests
    TOKEN = "5779297459:AAE2k4xaLnQZW0MRSmu0OX3UYftw7vZishg"
    chat_id = "-1001546918854"
    message = "DX de abertura alterado para"
    result = '{:.3f}'.format(result_min)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message} {result_abe}"
    print(requests.get(url).json()) # this sends the message
    pass

else:
    print("igual")   
