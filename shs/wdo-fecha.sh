#!/bin/bash
cd ~/pontos
mv cypress/e2e/* cypress/
mv cypress/wdo-fecha.cy.js cypress/e2e/
npm install

i=1

while [[ $i -lt 10 ]] 
do
        npm start
        if [ "$?" == '0' ]
           then
           if [ -s "arquivos/wdo-fecha.txt" ]; then
           break
           fi
        fi
echo "$i tentativa(s)"
((i++))
done
echo "$i" > logs/wdo-fecha.log
