#!/bin/bash
#
cd ~/pontos
diff package-cme.json package-cme-bkp.json
   if [ "$?" != '0' ]
   then
        cp package-cme-bkp.json package-cme.json
   fi