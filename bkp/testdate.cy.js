/// <reference types="cypress" />


describe('WDOH24', function (){
    //Cypress.config('defaultCommandTimeout', 100000);
    it('capturar dados wdo', function(){
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
          
          //console.log(Object.values(object1)[mes]);
        cy.log(Object.values(object1)[mes]);
        var letra = Object.values(object1)[mes]
        cy.log(mes)
        cy.log(ano)
       // cy.visit(`http://test.com/aaa/bbb?id=${idp}`)
        cy.visit(`https://br.advfn.com/bolsa-de-valores/bmf/WDO${letra}${ano}/historico`)
       // cy.visit('https://br.advfn.com/bolsa-de-valores/bmf/WDO24/historico')
        //cy.log(dayjs().format('MM')) // DD/MM/YYYY
    })
})