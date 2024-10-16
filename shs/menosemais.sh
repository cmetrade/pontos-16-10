#!/bin/bash
cd ~/pontos
arquivo="arquivos/wdoD-2.txt"

i=1

while [[ $i -lt 5 ]] 
do
        if [ -e $arquivo ]; then
           python3 pys/maisum.py
           python3 pys/menosum.py
           break
        fi
echo "$i tentativa(s)"
((i++))
done
echo "$i" > logs/menosemais.log
