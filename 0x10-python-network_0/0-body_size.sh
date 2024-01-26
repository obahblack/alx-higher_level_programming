#!/bin/bash
# Display size of body of the reponse
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
