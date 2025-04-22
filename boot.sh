#!/bin/bash

echo The bash for Delix Starting using Bash File Script.
echo ----------------------------------------------------

while true; do
    read -p "DELIX0W:/mnt/: $ " input

    if [ "$input" == "launch > /mnt/delix/launch/" ]; then
        clear
        python main.py
    elif [ "$input" == "clear" ]; then
        clear
        echo The bash for Delix Starting using Bash File Script.
        echo ----------------------------------------------------
    elif [ "$input" == "exit" ]; then
        exit 0
    elif [ "$input" == "whoami" ]; then
        echo ------------------------------------
        echo "USER        USERNAME        HOST"
        echo "user        @delixuser      localhost"
        echo ------------------------------------
    elif [ "$input" == "whatusingrn" ]; then
        echo using now: bash
        echo ----------------- 
    else
        echo command not found: $input
        echo ----------------- 
    fi
done