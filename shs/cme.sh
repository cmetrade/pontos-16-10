#!/bin/bash
cd ~/pontos/
mv cypress/e2e/* cypress/
mv cypress/cme.cy.js cypress/e2e/
cp package.json package.json.bkp
cp package-cme.json package.json

i=1

while [[ $i -lt 5 ]] 
do
        npm install
        npm start
        if [ "$?" == '0' ]
           then
           if [ -s "arquivos/cme-open.txt" ]; then
                python3 pys/cme-abertura.py
                python3 pys/cme-high.py
                python3 pys/cme-low.py
                cp package.json package-cme.json
                cp package.json.bkp package.json
           break
           fi
        fi
echo "$i tentativa(s)"
((i++))
cp package.json package-cme.json
cp package.json.bkp package.json
done

echo "$i" >  logs/cme.log
