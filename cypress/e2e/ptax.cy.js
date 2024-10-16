/// <reference types="cypress" />

describe('PTAX', function (){
    it('capturar dados da última ptax', function(){
        cy.visit('https://ptax.bcb.gov.br/ptax_internet/consultarUltimaCotacaoDolar.do')
       
        cy.get('.fundoPadraoBClaro2 > :nth-child(3)').then(function(text2){
              cy.log(text2.text())
              cy.writeFile('arquivos/ptax.txt', text2.text())
        })
         
    })
})