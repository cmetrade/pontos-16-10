/// <reference types="cypress" />


describe('DX', function (){
  //Cypress.config('defaultCommandTimeout', 300);
    it('DX', function(){

       cy.visit("https://br.financas.yahoo.com/quote/DX-Y.NYB/history/")
       
          cy.get('tbody > :nth-child(1) > :nth-child(4) > span').then(function(text1){
            cy.log(text1.text())
            cy.writeFile('arquivos/dx-min.txt', text1.text())
           })

           cy.get('tbody > :nth-child(1) > :nth-child(3) > span').then(function(text2){
            cy.log(text2.text())
            cy.writeFile('arquivos/dx-max.txt', text2.text())
           })

           cy.get('tbody > :nth-child(1) > :nth-child(5) > span').then(function(text3){
            cy.log(text3.text())
            cy.writeFile('arquivos/dx-fechamento.txt', text3.text())
           })
           
           cy.get('tbody > :nth-child(1) > :nth-child(2) > span').then(function(text4){
            cy.log(text4.text())
            cy.writeFile('arquivos/dx-abertura.txt', text4.text())
           })
           
    })
})