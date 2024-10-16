/// <reference types="cypress" />
describe('USD-BRL', function (){

    it('USD-BRL', function(){
        //cy.visit('https://br.investing.com/currencies/usd-brl-historical-data')
        cy.visit('https://br.advfn.com/bolsa-de-valores/fx/USDBRL/historico')
    


            // LINHA 1
            //abertura 
           cy.get('[comp-id="167"] > .ag-cell-wrapper > .ag-cell-value').then(function(text1){
            cy.log(text1.text())
            cy.writeFile('arquivos/linha1-usd-brl-abertura.txt', text1.text(), {flag: "a+"})
            })

            //maxima 
            cy.get('[comp-id="333"] > .ag-cell-wrapper > .ag-cell-value').then(function(text2){
            cy.log(text2.text())
            cy.writeFile('arquivos/linha1-usd-brl-max.txt', text2.text(), {flag: "a+"})
            })

            //minima 
            cy.get('[comp-id="334"] > .ag-cell-wrapper > .ag-cell-value').then(function(text3){
            cy.log(text3.text())
            cy.writeFile('arquivos/linha1-usd-brl-min.txt', text3.text(), {flag: "a+"})
            })

            //data
            cy.get('#table_more_historical > .delight-bordered-content > .ag-root-wrapper > .ag-root-wrapper-body > .ag-root > .ag-body > .ag-body-viewport > .ag-center-cols-viewport > .ag-center-cols-container > .ag-row-first > .ag-column-first > .ag-cell-wrapper > .ag-cell-value').then(function(text4){
            cy.log(text4.text())
            cy.writeFile('arquivos/linha1-usd-brl-data.txt', text4.text(), {flag: "a+"})
            })
            

            // LINHA 2
            //abertura 
            cy.get('[comp-id="173"] > .ag-cell-wrapper > .ag-cell-value').then(function(text5){
            cy.log(text5.text())
            cy.writeFile('arquivos/linha2-usd-brl-abertura.txt', text5.text(), {flag: "a+"})
            })

            //maxima 
            cy.get('[comp-id="336"] > .ag-cell-wrapper > .ag-cell-value').then(function(text6){
            cy.log(text6.text())
            cy.writeFile('arquivos/linha2-usd-brl-max.txt', text6.text(), {flag: "a+"})
            })

            //minima 
            cy.get('[comp-id="337"] > .ag-cell-wrapper > .ag-cell-value').then(function(text7){
            cy.log(text7.text())
            cy.writeFile('arquivos/linha2-usd-brl-min.txt', text7.text(), {flag: "a+"})
            })

            //data
            cy.get('[comp-id="168"] > .ag-column-first > .ag-cell-wrapper > .ag-cell-value').then(function(text8){
            cy.log(text8.text())
            cy.writeFile('arquivos/linha2-usd-brl-data.txt', text8.text(), {flag: "a+"})
            }) 

            //LINHA 3
            //abertura 
            cy.get('[comp-id="179"] > .ag-cell-wrapper > .ag-cell-value').then(function(text6){
            cy.log(text6.text())
            cy.writeFile('arquivos/linha3-usd-brl-abertura.txt', text6.text(), {flag: "a+"})
            })

            //maxima 
            cy.get('[comp-id="339"] > .ag-cell-wrapper > .ag-cell-value').then(function(text7){
            cy.log(text7.text())
            cy.writeFile('arquivos/linha3-usd-brl-max.txt', text7.text(), {flag: "a+"})
            })

            //minima 
            cy.get('[comp-id="340"] > .ag-cell-wrapper > .ag-cell-value').then(function(text8){
            cy.log(text8.text())
            cy.writeFile('arquivos/linha3-usd-brl-min.txt', text8.text(), {flag: "a+"})
            })

            //data
            cy.get('[comp-id="174"] > .ag-column-first > .ag-cell-wrapper > .ag-cell-value').then(function(text9){
            cy.log(text9.text())
            cy.writeFile('arquivos/linha3-usd-brl-data.txt', text9.text(), {flag: "a+"})
            })     
    }) 
})