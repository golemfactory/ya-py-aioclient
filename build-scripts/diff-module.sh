#! /bin/bash

NAME=$1
PATCH_NAME=$2

test -n "$NAME" || exit 1

diff -r -c "target/ya_$NAME" "src/ya_$NAME"
