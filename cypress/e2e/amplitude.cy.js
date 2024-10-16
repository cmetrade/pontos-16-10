/// <reference types="cypress" />

describe('AMPLITUDE', function (){
    it('capturar a amplitude da B3', function(){
        cy.visit('https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-de-derivativos/precos-referenciais/superficie-de-volatilidade-de-dolar/')
        cy.get('tbody > :nth-child(1) > :nth-child(7) ').then(function(text1){
              cy.log(text1.text())
              cy.writeFile('arquivos/amplitude.txt', text1.text())
        })

    })
})