/// <reference types="cypress" />
describe('CME', function (){
//Cypress.config('defaultCommandTimeout', 700);

    it('capturar dados cme yahoo', function(){
        
        cy.visit('https://www.cmegroup.com/markets/fx/emerging-market/brazilian-real.quotes.html#venue=globex', {   headers: {     "Accept-Encoding": "gzip, deflate"   } }, { timeout: 80000 })



            // open
            cy.get(':nth-child(1) > :nth-child(7) > .table-cell').then(function(text1){
            cy.log(text1.text())
            cy.writeFile('arquivos/cme-open.txt', text1.text())
            })
            
            //high
            cy.get(':nth-child(1) > :nth-child(8) > .table-cell').then(function(text2){
            cy.log(text2.text())
            cy.writeFile('arquivos/cme-high.txt', text2.text())
            })

            //low
            cy.get(':nth-child(1) > :nth-child(9) > .table-cell').then(function(text3){
            cy.log(text3.text())
            cy.writeFile('arquivos/cme-low.txt', text3.text())
            })

        })
})
   