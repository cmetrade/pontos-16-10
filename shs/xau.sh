#!/bin/bash
cd ~/pontos
rm arquivos/xau-max.txt arquivos/xau-min.txt
mv cypress/e2e/* cypress/
mv cypress/xau.cy.js cypress/e2e/
npm install

i=1

while [[ $i -lt 10 ]] 
do
        npm start
        if [ "$?" == '0' ]
           then
           if [ -s "arquivos/xau-max.txt" ]; then
           
           python3 pys/xau-alta.py
           python3 pys/xau-baixa.py 
           break
           fi
        fi
echo "$i tentativa(s)"
((i++))
done
echo "$i" > logs/xau.log
