#!/bin/bash
# Display size of body of the reponse
curl -sI "$1" | grep 'content-Length:' | cut -f2 -d' '
