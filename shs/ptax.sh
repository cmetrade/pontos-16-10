#!/bin/bash
cd ~/pontos
mv cypress/e2e/* cypress/
mv cypress/ptax.cy.js cypress/e2e/
npm install

i=1

while [[ $i -lt 5 ]] 
do
        npm start
        if [ "$?" == '0' ]
           then
           if [ -s "arquivos/ptax.txt" ];then
           python3 pys/ptax.py
           break
           fi
        fi
echo "$i tentativa(s)"
((i++))
done
echo "$i" > logs/ptax.log
