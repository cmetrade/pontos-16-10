#!/bin/bash
#
cd ~/pontos
mv cypress/e2e/* cypress/
mv cypress/cupom.cy.js cypress/e2e/
npm install

i=1

while [[ $i -lt 5 ]] 
do
        npm start
        if [ "$?" == '0' ]
           then
        if [ -s "arquivos/cupom.txt" ];then
           awk {'print $1 " |" ,$3 " |",$5'} arquivos/cupom.txt > arquivos/cupom2.txt 
           python3 pys/cupom.py
           break
        fi
        fi
echo "$i tentativa(s)"
((i++))
done
echo "$i" > logs/cupom.log