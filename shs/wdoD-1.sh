cd ~/pontos
mv cypress/e2e/* cypress/
mv cypress/wdoD-1.cy.js cypress/e2e/
npm install

i=1

while [[ $i -lt 11 ]] 
do
        npm start
        if [ "$?" == '0' ]
           then
           if [ -s "arquivos/wdoD-1.txt" ]; then
           break
           fi
        fi
echo "$i tentativa(s)"
((i++))
done
echo "$i" > logs/wdoD-1.log
