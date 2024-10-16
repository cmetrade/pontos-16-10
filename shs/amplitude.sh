#!/bin/bash
cd ~/pontos
mv cypress/e2e/* cypress/
mv cypress/amplitude.cy.js cypress/e2e/
npm install

i=1

while [[ $i -lt 11 ]] 
do
        npm start
        if [ "$?" == '0' ]
           then
           if [ -s "arquivos/amplitude.txt" ];then
           python3 pys/amplitude.py
           break
           fi
        fi
echo "$i tentativa(s)"
((i++))
done
echo "$i" > logs/amplitude.log
