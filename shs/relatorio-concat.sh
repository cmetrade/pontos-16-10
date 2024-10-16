#!/bin/bash
cd ~/pontos/logs
ptax=`cat ptax.log`
cme=`cat cme.log`
cupom=`cat cupom.log`
dx=`cat dx.log`
menosemais=`cat menosemais.log`
usdbrl=`cat usd-brl.log`
wdofecha=`cat wdo-fecha.log`
wdoD1=`cat wdoD-2.log`
xau=`cat xau.log`

echo " " > relatorio.log
echo " " >> relatorio.log
echo "PTAX = $ptax" >> relatorio.log
echo "CME = $cme" >> relatorio.log
echo "CUPOM = $cupom" >> relatorio.log
echo "MENOS E MAIS = $menosemais" >> relatorio.log
echo "USD/BRL = $usdbrl" >> relatorio.log
echo "FECHAMENTO WDO = $wdofecha" >> relatorio.log
echo "WDO D -1 = $wdoD1" >> relatorio.log
echo "XAU = $xau" >> relatorio.log
echo "DX = $dx" >> relatorio.log
echo " " >> relatorio.log
echo " " >> relatorio.log