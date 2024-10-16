#!/bin/bash

#sudo apt-get install -y libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb bc
cd ~/pontos
rm arquivos/*.txt
mv cypress/*.js cypress/e2e/
mv cypress/e2e/cme.cy.js cypress/
mv cypress/e2e/dx.cy.js cypress/
mv cypress/e2e/wdoG.cy.js cypress/
mv cypress/e2e/xau.cy.js cypress/
mv cypress/e2e/menosemais.cy.js cypress/
mv cypress/e2e/usd-brl.cy.js cypress/
mv cypress/e2e/cupom.cy.js cypress/
npm install
npm start
