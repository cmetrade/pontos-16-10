/// <reference types="cypress" />
describe('USD-BRL-SEGUNDA', function (){

    it('USD-BRL-SEGUNDA', function(){
       cy.visit('https://br.investing.com/currencies/usd-brl-historical-data')

            //abertura 
            cy.get('.p-0 > .w-full > tbody > :nth-child(2) > :nth-child(3)').then(function(text1){
            cy.log(text1.text())
            cy.writeFile('arquivos/usd-brl-segunda-abertura.txt', text1.text(), {flag: "a+"})
            })

            //maxima 
            cy.get('.p-0 > .w-full > tbody > :nth-child(2) > :nth-child(4)').then(function(text2){
            cy.log(text2.text())
            cy.writeFile('arquivos/usd-brl-segunda-max.txt', text2.text(), {flag: "a+"})
            })

            //minima 
            cy.get('.w-full > tbody > :nth-child(2) > :nth-child(5)').then(function(text3){
            cy.log(text3.text())
            cy.writeFile('arquivos/usd-brl-segunda-min.txt', text3.text(), {flag: "a+"})
            })
 
    })
})
   