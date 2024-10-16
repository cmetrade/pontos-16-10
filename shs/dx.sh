#!/bin/bash
cd ~/pontos
mv cypress/e2e/* cypress/
mv cypress/dx.cy.js cypress/e2e/
npm install

i=1

while [[ $i -lt 10 ]] 
do
        npm start
        if [ "$?" == '0' ]; then
           if [ -s "arquivos/dx-fechamento.txt" ]; then
              dxmax=`cat arquivos/dx-max.txt`
              dxmin=`cat arquivos/dx-min.txt`
                  if [ $dxmax != $dxmin ]; then
                     python3 pys/dx-alta.py
                     python3 pys/dx-baixa.py
                     python3 pys/dx-abertura.py 
                     break
                  fi
           fi
        fi
echo "$i tentativa(s)"
((i++))
echo "falhou" > logs/dx.log
done
echo "$i" >> logs/dx.log
