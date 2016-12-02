#!/bin/bash

set -e

IP=`docker-machine ip`
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

if [ "$1" == "test" ]; then
    docker run \
        vegadns2-public \
        /var/www/vegadns2/docker/start.sh \
        test
else
    docker run \
        -p 80:80 \
        -p 53:53/udp \
        -e IP=${IP} \
        vegadns2-public
fi
