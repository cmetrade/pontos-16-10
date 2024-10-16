#!/bin/bash
cd ~/pontos/
mv cypress/e2e/* cypress/
mv cypress/cme.cy.js cypress/e2e/
ls arquivos/cme-high.txt


    if [ $? -eq 0 ]; then
       mv arquivos/cme-high.txt arquivos/cme-high-old.txt
       mv arquivos/cme-low.txt arquivos/cme-low-old.txt
       npm install
    fi

valid=true
count=1

        while [ $valid ]
        do
            mv cypress/e2e/* cypress/
            mv cypress/cme.cy.js cypress/e2e/
            python3 pys/follow-cme.py
            mv arquivos/cme-high.txt arquivos/cme-high-old.txt
            mv arquivos/cme-low.txt arquivos/cme-low-old.txt
            npm start

            if [ $count -eq 5 ];
            then
            break
            fi
        ((count++))
        echo $count
        sleep 60
        done