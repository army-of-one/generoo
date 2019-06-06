#!/bin/bash

repository={{group_id_dashes}}
image={{artifact_id}}
version=LATEST

if [[ ! -z "$1" ]]; then
    repository=$1
fi

if [[ ! -z "$2" ]]; then
    image=$2
fi

if [[ ! -z "$3" ]]; then
    version=$3
fi

docker build -t $repository/$image:$version -f ../deploy/Dockerfile ..