#!/bin/bash

if [ $# -eq 0 ]
then
    echo "No arguments supplied, use --help for more info"
    exit 1
elif [ "$1" == "--help" ]
then
    echo "Usage: envar_set.sh <dev|local|prod>"
    exit 1
elif [ "$1" == "dev" ]
then
    echo "Setting development environment"
    export APP_ENV=dev
elif [ "$1" == "local" ]
then
    echo "Setting local environment"
    export APP_ENV=local
elif [ "$1" == "prod" ]
then
    echo "Setting production environment"
    export APP_ENV=prod
else
    echo "Invalid argument supplied, use --help for more info"
    exit 1
fi
