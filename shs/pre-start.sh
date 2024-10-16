#!/bin/bash

cd ~/pontos/shs/
# Nome do processo que você deseja verificar
PROCESSO="start.sh"

# Comando que será executado caso o processo não esteja rodando
COMANDO="./start.sh"

# Verifica se o processo está rodando
if ! pgrep -x "$PROCESSO" > /dev/null
then
    echo "O processo $PROCESSO não está em execução. Executando o comando..."
    $COMANDO
else
    echo "O processo $PROCESSO está em execução."
fi