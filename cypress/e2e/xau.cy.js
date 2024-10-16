/// <reference types="cypress" />
describe('XAU ', function (){
   
    it('capturar dados xau', function(){
        cy.visit('https://br.advfn.com/bolsa-de-valores/pm/XAUUSD/cotacao')
       
        
       //cy.visit('https://br.investing.com/currencies/xau-usd-historical-data')
            cy.get(':nth-child(2) > :nth-child(5) > .text-semibold').then(function(text2){
                cy.log(text2.text())
                cy.writeFile('arquivos/xau-min.txt', text2.text(), {flag: "a+"})
           })
            cy.get(':nth-child(2) > :nth-child(4) > .text-semibold').then(function(text3){
                cy.log(text3.text())
                cy.writeFile('arquivos/xau-max.txt', text3.text(), {flag: "a+"})
            })
        
    })
})
   