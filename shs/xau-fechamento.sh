#!/bin/bash
cd ~/pontos
rm arquivos/xau-fechamento.txt
mv cypress/e2e/* cypress/
mv cypress/xau-fechamento.cy.js cypress/e2e/
npm install

i=1

while [[ $i -lt 5 ]] 
do
        npm start
        if [ "$?" == '0' ]
           then
           if [ -s "arquivos/xau-fechamento.txt" ]; then
           break
           fi
        fi
echo "$i tentativa(s)"
((i++))
done
echo "$i" > logs/xau-fechamento.log
