#!/bin/bash

# Nome do arquivo de entrada
input_file="frases.txt"
# Nome do arquivo de saída
output_file="frases_sem_aspas.txt"

# Verifica se o arquivo de entrada existe
if [ ! -f "$input_file" ]; then
    echo "O arquivo $input_file não existe."
    exit 1
fi

# Remove aspas tipográficas e salva no arquivo de saída
sed 's/“//g; s/”//g' "$input_file" > "$output_file"

echo "Aspas tipográficas removidas e salvas em $output_file."
