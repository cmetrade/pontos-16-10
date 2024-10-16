#!/bin/bash
#
cd ~/pontos/arquivos
 echo "DATA                    ABE                MAX               MIN" > usd-brl.txt
 echo "$(cat linha1-usd-brl-data.txt) $(echo '        ') $(cat linha1-usd-brl-abertura.txt)  $(echo '        ') $(cat linha1-usd-brl-max.txt)  $(echo '        ') $(cat linha1-usd-brl-min.txt)" >> usd-brl.txt
 echo "$(cat linha2-usd-brl-data.txt) $(echo '        ') $(cat linha2-usd-brl-abertura.txt)  $(echo '        ') $(cat linha2-usd-brl-max.txt)  $(echo '        ') $(cat linha2-usd-brl-min.txt)" >> usd-brl.txt
 echo "$(cat linha3-usd-brl-data.txt) $(echo '        ') $(cat linha3-usd-brl-abertura.txt)  $(echo '        ') $(cat linha3-usd-brl-max.txt)  $(echo '        ') $(cat linha3-usd-brl-min.txt)" >> usd-brl.txt
