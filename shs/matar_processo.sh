#!/bin/bash

# Tempo mínimo em minutos para identificar processos antigos
MIN_TIME=10

# Encontra processos com mais de 10 minutos
echo "Processos rodando há mais de $MIN_TIME minutos:"
ps -eo pid,etime,comm --sort=-etime |grep start.sh| grep -E "([0-9]+-)?([1-9][0-9]:)?[1-9][0-9]:[0-9]{2}" | while read -r line; do
    pid=$(echo $line | awk '{print $1}')
    elapsed_time=$(echo $line | awk '{print $2}')
    
    # Converte o tempo para minutos
    if [[ $elapsed_time =~ ([0-9]+)-([0-9]{2}):([0-9]{2}):([0-9]{2}) ]]; then
        days=${BASH_REMATCH[1]}
        hours=${BASH_REMATCH[2]}
        minutes=${BASH_REMATCH[3]}
    elif [[ $elapsed_time =~ ([0-9]{2}):([0-9]{2}):([0-9]{2}) ]]; then
        days=0
        hours=${BASH_REMATCH[1]}
        minutes=${BASH_REMATCH[2]}
    elif [[ $elapsed_time =~ ([0-9]{2}):([0-9]{2}) ]]; then
        days=0
        hours=0
        minutes=${BASH_REMATCH[1]}
    fi
    
    total_minutes=$(( days * 1440 + hours * 60 + minutes ))

    # Verifica se o processo está rodando há mais de MIN_TIME minutos
    if [ $total_minutes -ge $MIN_TIME ]; then
        echo "Matando processo PID $pid rodando há $total_minutes minutos ($elapsed_time)"
        kill -9 $pid && echo "Processo $pid finalizado." || echo "Falha ao finalizar o processo $pid."
    fi
done