#!/bin/bash
#
cd ~/pontos
rm arquivos/linha*
mv cypress/e2e/* cypress/
mv cypress/usd-brl.cy.js cypress/e2e/

npm install
i=1

        while [[ $i -lt 5 ]]
        do
        npm start
        if [ "$?" == '0' ]
           then
                ./shs/usd-brl-format.sh
                python3 pys/usd-brl.py
                break
        fi
        echo "$i tentativa(s)"
        ((i++))
        done
        echo "$i" > logs/usd-brl.log