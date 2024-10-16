#!/bin/bash
cd ~/pontos/
mv cypress/e2e/* cypress/
mv cypress/dx.cy.js cypress/e2e/
ls arquivos/dx-max.txt

    if [ $? -eq 0 ]; then
       mv arquivos/dx-max.txt arquivos/dx-max-old.txt
       mv arquivos/dx-min.txt arquivos/dx-min-old.txt
       mv arquivos/dx-abertura.txt arquivos/dx-abertura-old.txt
       npm start
    fi

valid=true
count=1

        while [ $valid ]
        do
            mv cypress/e2e/* cypress/
            mv cypress/dx.cy.js cypress/e2e/
            python3 pys/follow-dx.py
            mv arquivos/dx-max.txt arquivos/dx-max-old.txt
            mv arquivos/dx-min.txt arquivos/dx-min-old.txt
            mv arquivos/dx-abertura.txt arquivos/dx-abertura-old.txt
            npm start

            if [ $count -eq 5 ];
            then
            break
            fi
        ((count++))
        echo $count
        sleep 60
        done