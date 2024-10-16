#!/bin/bash
#
cd ~/pontos
diff package.json package-orig.json

   if [ "$?" != '0' ]
   then
        cp package-orig.json package.json
   fi