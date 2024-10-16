/// <reference types="cypress" />

describe('WDO - fechamento D -1', function (){
    it('capturar dados de fechamento wdo', function(){
        const dayjs = require('dayjs')
        const mes = dayjs().format('M')
        const ano = dayjs().format('YY')

        const object1 = {
            a: 'F',
            b: 'G',
            c: 'H',
            d: 'J',
            e: 'K',
            f: 'M',
            g: 'N',
            h: 'Q',
            i: 'U',
            j: 'V',
            k: 'X',
            l: 'Z',
          };
        var letra = Object.values(object1)[mes]

        cy.visit(`https://br.advfn.com/bolsa-de-valores/bmf/WDO${letra}${ano}/historico`)
        cy.get('[comp-id="164"] > .ag-cell-wrapper > .ag-cell-value').then(function(text2){
       // cy.get(':nth-child(8) > table > tbody > :nth-child(3) > :nth-child(2)').then(function(text2){
              cy.log(text2.text())
              cy.writeFile('arquivos/wdoD-2.txt', text2.text())
        })
          
    })
})