/// <reference types="cypress" />

describe('PTAX-FUTURO', function (){
    it('capturar dados da última ptax-futuro', function(){
        cy.visit('https://sistemaswebb3-derivativos.b3.com.br/financialIndicatorsPage/')

        cy.get(':nth-child(2) > .col > :nth-child(2) > .mb-2').then(function(text2){
              cy.log(text2.text())
              cy.writeFile('arquivos/ptax-futuro.txt', text2.text())
        })

    })
})