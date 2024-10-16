/// <reference types="cypress" />
describe('XAU Fechamento', function (){
   
    it('capturar dados do fechamento do xau', function(){
        cy.visit('https://br.advfn.com/bolsa-de-valores/pm/XAUUSD/historico')
            
            cy.get('[comp-id="164"] > .ag-cell-wrapper > .ag-cell-value').then(function(text4){
                cy.log(text4.text())
                cy.writeFile('arquivos/xau-fechamento.txt', text4.text(), {flag: "a+"})
            })
                
    })
})
   