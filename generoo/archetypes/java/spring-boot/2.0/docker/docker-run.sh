#!/bin/bash

env=local
version=LATEST

if [[ ! -z "$1" ]]; then
    env=$1
fi

if [[ ! -z "$2" ]]; then
    version=$2
fi

docker run -e "ENV=$env" -p "8080:8080" {{group_id_dashes}}/{{artifact_id}}:$version