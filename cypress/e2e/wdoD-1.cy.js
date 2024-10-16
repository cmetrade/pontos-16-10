/// <reference types="cypress" />

describe('WDO - Abertura D -1', function (){
    it('capturar dados de abertura wdo', function(){
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
        //cy.visit('https://br.advfn.com/bolsa-de-valores/bmf/WDOM24/historico')
       
        cy.get(':nth-child(8) > table > tbody > :nth-child(3) > :nth-child(2)').then(function(text2){
              cy.log(text2.text())
              cy.writeFile('arquivos/wdoD-1.txt', text2.text())
        })
          
    })
})